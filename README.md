# AI Trip Planner 🌍

> AI-powered travel planner and expense estimator that generates detailed, day-by-day travel plans using live data (places, weather, currency rates) and modular tools.

---

## ✨ Overview

**AI Trip Planner** helps users plan trips by combining an agentic workflow (LangGraph / LangChain style) with real-time tools for:

- Places & attractions (Google Places / Tavily fallback)
- Weather forecasts (OpenWeatherMap)
- Currency conversion (exchange rate API)
- Expense calculation and budgets

It exposes a FastAPI backend that runs the planner agent and a small Streamlit frontend to interact with it.

---

## 🚀 Quick Start

Prerequisites:

- Python 3.11+
- Make sure you have API keys for any services you intend to use (Google Places, OpenWeatherMap, Exchange Rate API). Add them to a `.env` file at the project root.

Install dependencies (recommended in a virtual environment):

```pwsh
python -m pip install -r requirements.txt
# or editable install
python -m pip install -e .
```

Create a `.env` with the following keys (example):

```text
GPLACES_API_KEY=your_google_places_key
OPENWEATHERMAP_API_KEY=your_openweather_key
EXCHANGE_RATE_API_KEY=your_exchange_rate_key
# any model provider keys if required (e.g., GROQ/OPENAI)
```

Run the backend API:

```pwsh
uvicorn main:app --reload --port 8000
```

Start the Streamlit UI (optional):

```pwsh
streamlit run streamlit_app.py
```

Open http://localhost:8501 for the Streamlit UI or call the API directly at `POST http://localhost:8000/query` with JSON `{"question": "Plan a trip to Goa for 5 days"}`.

---

## 🧩 Key Features

- Agentic planner that composes multiple tool calls to produce complete travel plans
- Two-plan style: mainstream tourist plan + off-beat alternatives (configured in the system prompt)
- Detailed itinerary: day-by-day, hotels, restaurants, activities, transport modes
- Expense breakdown: hotel cost estimation, daily budget, full trip totals
- Export to Markdown files for sharing or archiving

---

## 🏗️ Architecture

- FastAPI backend (`main.py`) — receives user prompts and invokes the agent graph
- Agent builder (`agent/agentic_workflow.py`) — wires an LLM to a set of tools (weather, places, currency, calculator)
- Tools (`tools/*`) — small wrappers around real APIs and helper utilities
- Streamlit UI (`streamlit_app.py`) — lightweight frontend to send queries to the backend
- Utilities (`utils/*`) — conversion, expense calculator, document export, and model loader

---
