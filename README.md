# WanderWise-AITravelPlanner
An AI-powered travel planner that suggests destinations, creates itineraries, and helps organize your trips—built to explore how AI can simplify travel planning!

## 🚀 Features

- 🗺️ **Trip Planner**: Creates customized travel plans based on your preferences and location.
- 🍜 **Cuisine Recommender**: Suggests local foods and dishes based on destination.
- 💸 **Budget Estimator**: Breaks down estimated expenses (travel, stay, food, etc.).
- 🚨 **Emergency Assistant**: Provides quick access to emergency info like hospitals, embassies, and police.
- 💱 **Currency Converter**: Converts currencies using real-time exchange rates.
- 📍 **Map Integration**: Displays location-based info using interactive maps.

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) (with multipage support & sidebar UI)
- **Backend**: Python (using [LangChain](https://www.langchain.com/), [CrewAI](https://docs.crewai.com/), and [Groq API](https://console.groq.com/))
- **APIs Used**:
  - **Groq API** (for fast LLM responses)
  - **Open Exchange Rates API** (for currency conversion)
  - **Nominatim (Geopy)** (for location-based services)
- **Others**:
  - `streamlit-folium` for map rendering
  - `pandas` for data handling
  - `dotenv` for managing API keys securely
## 📁 Project Structure
  ai-travel-planner/
│
├── .env # API keys stored securely
├── main.py # Entry point for Streamlit app
├── README.md # Project documentation
│
├── agents/ # CrewAI agents for each feature
│ ├── budget_estimator.py
│ ├── trip_planner.py
│ ├── cuisine_recommendor.py
│ └── emergency_assistant.py
│
├── pages/ # Streamlit pages (UI)
│ ├── 1_Trip_Planner.py
│ ├── 2_Cuisine_Recommender.py
│ ├── 3_Budget_Planner.py
│ ├── 4_Emergency_Assistant.py
│ └── 5_Currency_Converter.py
│
├── services/ # Tasks and functional service logic
│ ├── service.py
│ └── task.py
│
└── utils/ # Utility modules and helpers
├── auth.py
├── config.py
├── session_state.py
├── currency_utils.py
├── map_utils.py
└── weather_utils.py


## ✅ Setup Instructions

**Step 1: Clone the repository**
git clone https://github.com/yourusername/ai-travel-planner.git
cd ai-travel-planner

**Step 2: Create a virtual environment (optional but recommended)**
python -m venv venv
source venv/bin/activate   # For Linux/Mac
**venv\Scripts\activate      # For Windows**

**Step 3: Install dependencies**
pip install -r requirements.txt

**Step 4: Set up environment variables**
 - Create a .env file in the root of the project.
 - Add your API keys and any necessary configurations:
   GROQ_API_KEY=your_groq_api_key

**Step 5: Run the application**
streamlit run main.py

**Step 6: Visit the app**
**- Open the link provided by Streamlit in your browser (usually http://localhost:8501).**

## 🧠 Powered By
This project uses a combination of powerful tools and technologies:

LangChain: A framework for developing applications powered by LLMs (Large Language Models).

CrewAI: A service for managing multiple AI agents that collaborate to complete complex tasks.

Groq: High-performance LLMs optimized for fast response times.

Streamlit: A web framework for building and deploying interactive web apps with Python.

Geopy: A Python library for geocoding and location-based services.

Open Exchange Rates API: API for real-time currency conversion rates.

streamlit-folium: A wrapper to display interactive maps with Folium in Streamlit.
