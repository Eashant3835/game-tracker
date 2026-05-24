🎯 The Valorant Coach
An AI-powered Valorant coaching web app that analyzes your match history and delivers personalized, data-driven feedback to help you improve.
Live Demo: valorant-coach.onrender.com

Features

Match History Analysis — Fetches your last 20 matches via the HenrikDev Valorant API
AI Coaching — Uses Groq (llama-3.3-70b-versatile) to generate personalized coaching advice backed by your actual stats
Economy Insights — Tracks average credits spent and loadout value per match
Multi-Region Support — Works across NA, EU, AP, LATAM, BR, and KR servers
Match Persistence — Stores player and match data in a SQLite database


Tech Stack
LayerTechnologyBackendPython, FlaskFrontendHTML, CSS, JavaScriptDatabaseSQLiteAIGroq API (llama-3.3-70b-versatile)Game DataHenrikDev Valorant APIDeploymentRender

How It Works

User enters their Valorant username, tag, and region
The app fetches their PUUID and last 20 matches from the HenrikDev API
Match data is parsed and key stats are extracted (KDA, headshot %, damage, economy, ability usage)
Aggregated stats and match-by-match data are sent to Groq's LLM with a structured coaching prompt
The AI returns 5 specific, actionable coaching tips backed by real match references
Results are displayed and saved to the database


Getting Started
Prerequisites

Python 3.10+
A HenrikDev API key
A Groq API key

Installation
bash# Clone the repo
git clone https://github.com/Eashant3835/game-tracker.git
cd game-tracker

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
Environment Variables
Create a .env file in the backend/ directory:
HENRIK_API_KEY=your_henrikdev_api_key
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.3-70b-versatile
Run Locally
bashcd backend
python app.py
Visit http://localhost:5000 in your browser.

Project Structure
game-tracker/
├── backend/
│   ├── app.py            # Flask routes
│   ├── valorant_api.py   # HenrikDev API integration & match parsing
│   ├── ai.py             # Groq AI coaching logic
│   ├── database.py       # SQLite setup and queries
│   └── .env              # Environment variables (not committed)
├── frontend/
│   ├── index.html
│   └── style.css
└── README.md

Example Output

Focus on crosshair placement — your headshot % sits at 17.1%, highlighted by your Jett game on Skirmish A where you got 0 headshots across 10 kills.


Be more selective with engagements on Haven — your Cypher game showed 33 kills but 17 deaths, suggesting you were taking unnecessary duels late in rounds.


Limitations

Requires the account to be indexed in HenrikDev's database
Match outcome may show as "Unknown" for non-standard game modes
No rank context — stats are not adjusted for lobby difficulty

Demo

<img width="1901" height="895" alt="image" src="https://github.com/user-attachments/assets/02d401c1-3ec8-452c-9378-42abf3e43778" />



License
MIT
