import os
import pandas as pd
import plotly.express as px
import plotly.io as pio
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from deep_translator import GoogleTranslator
from dotenv import load_dotenv
import json
import traceback

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")
USE_MOCK_DATA = os.getenv("USE_MOCK_DATA", "true").lower() == "true"

# Initialize FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DataFrame for mock data
if USE_MOCK_DATA:
    df = pd.read_csv("mock_ga_data.csv")
    df["date"] = pd.to_datetime(df["date"])
else:
    # Placeholder for GA4 data (not used with mock data)
    df = None

# Initialize LLM
llm = ChatOpenAI(
    model="meta-llama/llama-3.1-8b-instruct:free",
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL
)

# Initialize translator
translator = GoogleTranslator(source='auto')

# Pydantic model for request
class QueryRequest(BaseModel):
    query: str
    language: str

# Translate text
def translate_text(text, target_lang):
    if target_lang == "en":
        return text
    try:
        return translator.translate(text, dest=target_lang)
    except Exception:
        return text

# Generate Plotly chart
def generate_chart(query, df):
    if "trend" in query.lower() or "over time" in query.lower():
        metrics = []
        if "sessions" in query.lower():
            metrics.append("sessions")
        if "users" in query.lower():
            metrics.append("users")
        if "pageviews" in query.lower():
            metrics.append("pageviews")
        if "bounce rate" in query.lower():
            metrics.append("bounce_rate")
        if "event count" in query.lower():
            metrics.append("eventCount")
        if "active users" in query.lower():
            metrics.append("activeUsers")
        if not metrics:
            metrics = ["sessions", "users", "pageviews"]
        fig = px.line(
            df,
            x="date",
            y=metrics,
            title="Trends Over Time",
            labels={"value": "Count", "variable": "Metric"}
        )
        return pio.to_json(fig)
    return None

# Process query
@app.post("/query")
async def process_query(request: QueryRequest):
    try:
        query_en = translate_text(request.query, "en") if request.language != "en" else request.query

        # Use mock data (or fetch GA4 data if USE_MOCK_DATA=false)
        data_df = df  # Use the global df for mock data

        # Prepare data summary for prompt
        data_summary = data_df.to_string(index=False)

        # Define prompt
        prompt_template = PromptTemplate(
            input_variables=["input"],
            template=f"""
            You are a Business Intelligence assistant for non-technical SME owners in Asia.
            Below is a summary of the Google Analytics data for 2025, with columns: date, sessions, users, pageviews, bounce_rate, pagePath, source, medium, deviceCategory, eventCount, activeUsers, avgSessionDuration:

            {data_summary}

            Your task is to answer business questions based on this data.
            - Provide a clear, concise, and non-technical answer in plain text.
            - For trends or comparisons, include "[CHART]" to indicate a chart is available.
            - Suggest one relevant follow-up question.
            - Format numbers appropriately (e.g., percentages for bounce_rate).
            - Conclude with: "Final Answer: [answer]\nFollow-up: [question]"
            Answer: {{input}}
            """
        )

        # Run LLM
        response = llm.invoke(prompt_template.format(input=query_en)).content

        # Extract answer and follow-up
        if "Final Answer:" in response:
            parts = response.split("Final Answer:", 1)
            answer = parts[1].strip().split("\nFollow-up:")[0].strip()
            follow_up = parts[1].strip().split("\nFollow-up:")[1].strip() if "\nFollow-up:" in parts[1] else "Would you like more details?"
        else:
            answer = response.strip()
            follow_up = "Would you like more details?"

        # Generate chart
        chart_data = generate_chart(query_en, data_df)  # Pass data_df to generate_chart

        # Translate response
        response_translated = translate_text(answer, request.language)
        follow_up_translated = translate_text(follow_up, request.language)

        return {
            "response": response_translated,
            "chart": chart_data,
            "follow_up": follow_up_translated
        }
    except Exception as e:
        error_message = f"Error processing query: {str(e)}\n{traceback.format_exc()}"
        print(error_message)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)