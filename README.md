Business Intelligence Chatbot
A Business Intelligence (BI) chatbot designed for non-technical SME owners in Asia, providing insights from Google Analytics data through a conversational interface. The chatbot supports English, Mandarin (zh-cn), and Cantonese (zh-hk) queries, with responses including text and interactive Plotly charts for trends. It currently uses mock Google Analytics data for 365 days (2025) but can be extended to connect to the Google Analytics Data API (v1) for real GA4 data.
Features

Multilingual Support: Handles queries and responses in English, Mandarin, and Cantonese using deep-translator.
Data Insights: Answers questions about sessions, users, pageviews, bounce rate, event count, and more.
Interactive Charts: Generates Plotly line charts for trend queries (e.g., "Show the trend of sessions over time").
FastAPI Backend: Processes queries with a LangChain LLM (LLaMA 3.1 via OpenRouter) and serves data via REST API.
React Frontend: Displays chat interface and charts using react-plotly.js.
Mock Data: Uses mock_ga_data.csv (365 days, 2025) with realistic metrics and dimensions.
Git Management: Includes .gitignore to exclude sensitive and generated files.

Project Structure
bi-agent/
├── bi-agent-frontend/      # React frontend
│   ├── src/
│   │   ├── Chat.js        # Main chat component with Plotly charts
│   │   ├── Chat.css       # Styles for chat interface
│   │   ├── App.js         # Root React component
│   │   └── App.css        # Styles for app
│   ├── package.json       # Node.js dependencies
│   └── ...
├── main.py                # FastAPI backend with LLM and data processing
├── generate_mock_data.py  # Script to generate 365-day mock GA data
├── mock_ga_data.csv       # Mock Google Analytics data (generated)
├── summary_report.json    # Multilingual report (generated)
├── .gitignore             # Git ignore file
├── .env                   # Environment variables (not tracked)
├── README.md              # This file
└── venv/                  # Python virtual environment (not tracked)

Prerequisites

Python 3.12: For backend.
Node.js 16+: For frontend.
Git: For version control.
Google Analytics Data API (optional): For real GA4 data (not currently used).

Setup Instructions
Backend Setup

Clone the Repository:
git clone https://github.com/yourusername/bi-agent.git
cd bi-agent


Create Virtual Environment:
python -m venv venv
.\venv\Scripts\activate  # Windows


Install Python Dependencies:
pip install fastapi uvicorn pandas numpy plotly langchain-openai deep-translator python-dotenv


Set Environment Variables:Create a .env file in the root directory:
OPENAI_API_KEY=your_openai_key  # OpenRouter API key
OPENAI_BASE_URL=https://openrouter.ai/api/v1
USE_MOCK_DATA=true

Obtain an OpenRouter API key from openrouter.ai.

Generate Mock Data (if not already present):
python generate_mock_data.py

This creates mock_ga_data.csv with 365 days of data for 2025.


Frontend Setup

Navigate to Frontend Directory:
cd bi-agent-frontend


Install Node.js Dependencies:
npm install


Verify Dependencies:Ensure react-plotly.js and plotly.js are installed:
npm list react-plotly.js plotly.js



Running the Application

Start the Backend:
cd C:\Users\ashut\hongkong\bi-agent
.\venv\Scripts\activate
python main.py

The API will run at http://localhost:8000.

Start the Frontend:
cd bi-agent-frontend
npm start

The React app will open at http://localhost:3000.


Usage

Access the Chatbot: Open http://localhost:3000 in a browser.
Submit Queries:
English: "What was the bounce rate on July 15, 2025?" or "Show the trend of sessions over time."
Mandarin: "2025年1月的平均跳出率是多少？"
Cantonese: "2025年7月15號嘅跳出率係幾多？" or "2025年會話數同頁面瀏覽量嘅趨勢係點？"


View Responses: Text responses appear in the chat interface, with Plotly charts for trend queries.
Test API Directly:curl -X POST http://localhost:8000/query -H "Content-Type: application/json" -d "{\"query\":\"Show the trend of sessions over time\",\"language\":\"en\"}"



Testing
Test the following queries to verify functionality:

Specific Metric: "What was the bounce rate on July 15, 2025?" (English, no chart).
Trend: "Show the trend of sessions and pageviews over time" (English, with chart).
New Column: "What is the total event count for 2025?" (English, no chart).
Multilingual (Mandarin): "2025年1月的平均跳出率是多少？" (zh-cn, no chart).
Multilingual (Cantonese): "2025年會話數同頁面瀏覽量嘅趨勢係點？" (zh-hk, with chart).

Check the browser console (F12 > Console) and backend terminal for errors.
Deliverables

GitHub Repository: Contains all source code, excluding sensitive files (via .gitignore).
Screenshots: Capture frontend responses for the test queries, especially charts.
Multilingual Report: Generate summary_report.json:python -c "
from deep_translator import GoogleTranslator
import pandas as pd
import json
translator = GoogleTranslator(source='auto')
df = pd.read_csv('mock_ga_data.csv')
report = {
    'en': f'2025 Total sessions: {df['sessions'].sum()}, Avg bounce rate: {df['bounce_rate'].mean():.2%}',
    'zh-cn': translator.translate(f'2025总会话数: {df['sessions'].sum()}, 平均跳出率: {df['bounce_rate'].mean():.2%}', dest='zh-cn'),
    'zh-hk': translator.translate(f'2025總會話數: {df['sessions'].sum()}, 平均跳出率: {df['bounce_rate'].mean():.2%}', dest='zh-hk')
}
with open('summary_report.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
"



Troubleshooting

Backend Errors:
Ensure mock_ga_data.csv exists and has columns: date, sessions, users, pageviews, bounce_rate, etc.
Verify .env file and OpenRouter API key.


Frontend Errors:
Check react-plotly.js installation: npm list react-plotly.js.
Ensure CORS is enabled in main.py for http://localhost:3000.


Translation Issues:
Test deep-translator:from deep_translator import GoogleTranslator
print(GoogleTranslator(source='auto').translate("Test", dest="zh-hk"))





Future Improvements

Connect to real Google Analytics Data API (v1) for GA4 data (see main.py comments for setup).
Add support for custom date ranges (e.g., "Show sessions for Q1 2025").
Enhance frontend with responsive design and query history.

