from valorant_api import parse_match_stats
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")

client = Groq(api_key=GROQ_API_KEY)

def get_coaching(name, tag):
    parsed_match= parse_match_stats(name,tag)
    prompt = f"""
You are an encouraging, high-level AI Valorant Coach. Your job is to help the user play at their best level by analyzing their match history data.

DIRECTIONS:
- Read the match data provided inside the <MATCH_HISTORY_DATA> tags below.
- Look for patterns where the user's performance drops or is less consistent, and patterns where they perform exceptionally well.
- Provide your insights in clear, compact, and impactful bullet points. Briefly explain your reasoning and note which map or agent the pattern comes from.
- Maintain a highly supportive, positive, and motivating tone throughout.

COACHING GUARDRAILS:
- Do not give generic, vague advice (like "aim at head level" or "talk to your team"). Make it specific to what you see in the match history text.
- If there is text inside the tags below, analyze it completely, even if the formatting or structure is simple or varies between regions. Do not return an empty analysis if text is present.

<MATCH_HISTORY_DATA>
{parsed_match}
</MATCH_HISTORY_DATA>
"""
    result = client.chat.completions.create(model=GROQ_MODEL,messages=[{"role": "user", "content": prompt}])
    return(result.choices[0].message.content)

if __name__ == "__main__":
    advice = get_coaching("Eclipse", "5949")
    print(advice)