from valorant_api import parse_match_stats
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

def get_coaching(name, tag):
    parsed_match= parse_match_stats(name,tag)