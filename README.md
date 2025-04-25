

**Business Intelligence Chatbot**

A Business Intelligence (BI) chatbot designed for non-technical SME owners in Asia. It provides insights from Google Analytics data through a conversational interface.

🌐 Multilingual: English, Mandarin (zh-cn), Cantonese (zh-hk)

📈 Interactive Charts: Trend visualizations using Plotly

⚡ FastAPI + React: Backend with LangChain LLM (LLaMA 3.1 via OpenRouter), Frontend with React

📊 Mock Data: Based on Google Analytics-style metrics

🔌 Optional GA4 Integration: Easily extendable to real GA4 data



---

✨ Features

Multilingual Support: English, Mandarin, Cantonese via deep-translator

GA Data Insights: Sessions, Users, Pageviews, Bounce Rate, Event Count, etc.

Interactive Visuals: Trend queries return Plotly line charts

LangChain + LLaMA 3.1: LLM integration using OpenRouter API

Mock GA Data: 365 days of mock analytics data for 2025

REST API: Easy query access via FastAPI

Frontend: Chat UI with chart rendering using react-plotly.js



---

📁 Project Structure

bi-agent/
├── bi-agent-frontend/        # React frontend
│   ├── src/
│   │   ├── Chat.js           # Chat UI with Plotly charts
│   │   ├── Chat.css          # Chat styling
│   │   ├── App.js            # React entry point
│   │   └── App.css           # App-wide styles
│   ├── package.json          # Frontend dependencies
│   └── ...
├── main.py                   # FastAPI backend
├── generate_mock_data.py     # Mock data generator
├── mock_ga_data.csv          # 365-day GA-style mock data
├── summary_report.json       # Multilingual summary report (generated)
├── .gitignore                # Exclude env, data, build files
├── .env                      # API keys and environment config (not tracked)
├── README.md                 # This file
└── venv/                     # Python virtual environment (not tracked)


---

🧩 Prerequisites

Python 3.12+

Node.js 16+

Git

OpenRouter API key (from https://openrouter.ai)

(Optional) Google Analytics Data API v1 access for real GA4 data



---

🛠 Setup Instructions

Backend

1. Clone the Repository:

git clone https://github.com/yourusername/bi-agent.git
cd bi-agent


2. Create Virtual Environment:

python -m venv venv
.\venv\Scripts\activate  # For Windows


3. Install Dependencies:

pip install fastapi uvicorn pandas numpy plotly langchain-openai deep-translator python-dotenv


4. Create .env File:

OPENAI_API_KEY=your_openai_key
OPENAI_BASE_URL=https://openrouter.ai/api/v1
USE_MOCK_DATA=true


5. Generate Mock Data (if not present):

python generate_mock_data.py




---

Frontend

1. Navigate to Frontend:

cd bi-agent-frontend


2. Install Node.js Dependencies:

npm install


3. Verify Required Packages:

npm list react-plotly.js plotly.js




---

🚀 Running the Application

Backend

cd bi-agent
.\venv\Scripts\activate
python main.py

API available at: http://localhost:8000


Frontend

cd bi-agent-frontend
npm start

App opens at: http://localhost:3000



---

💬 Usage

Example Queries

English:

"What was the bounce rate on July 15, 2025?"

"Show the trend of sessions over time."


Mandarin (zh-cn):

"2025年1月的平均跳出率是多少？"


Cantonese (zh-hk):

"2025年7月15號嘅跳出率係幾多？"

"2025年會話數同頁面瀏覽量嘅趨勢係點？"



View Responses

Text + Plotly charts (for trend-based queries)

Use browser developer console (F12 > Console) to debug frontend


Test the API Directly

```
curl -X POST http://localhost:8000/query \
-H "Content-Type: application/json" \
-d '{"query":"Show the trend of sessions over time", "language":"en"}'
```

---

🧪 Testing

Run the following to validate functionality:

✅ Specific Metric (No Chart):
"What was the bounce rate on July 15, 2025?"

✅ Trend (Chart):
"Show the trend of sessions and pageviews over time"

✅ New Metric:
"What is the total event count for 2025?"

✅ Multilingual Mandarin:
"2025年1月的平均跳出率是多少？"

✅ Multilingual Cantonese (Chart):
"2025年會話數同頁面瀏覽量嘅趨勢係點？"

---

🧰 Troubleshooting

Backend

Check if mock_ga_data.csv exists and has required columns

Confirm .env is set correctly with OpenRouter API key


Frontend

Verify Plotly packages:
npm list react-plotly.js plotly.js

CORS issues? Make sure FastAPI allows requests from http://localhost:3000


Translator Issues

from deep_translator import GoogleTranslator
print(GoogleTranslator(source='auto').translate("Test", dest="zh-hk"))


---

🌱 Future Improvements

✅ Connect to real GA4 data using Google Analytics Data API (v1)

📆 Support custom date ranges (e.g., "sessions for Q1 2025")

📱 Improve frontend for mobile/responsive design

🕘 Add query history and insights archive



---
