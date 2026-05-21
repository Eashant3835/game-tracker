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
You are a strict Valorant Data Analyst and Performance Coach. Your task is to analyze ONLY the raw match history data provided below. 

CRITICAL GUARDRAILS AGAINST HALLUCINATION:
- You must maintain 100% data faithfulness to the text inside the <MATCH_HISTORY_DATA> tags.
- Do NOT assume, infer, or fabricate matches, maps, agents, or round events that are not explicitly documented in the data block.
- If the provided data is missing context (e.g., if a match doesn't specify the map or economy state), do NOT guess it. Only analyze the specific metrics present.
- Every single bullet point you output MUST begin with a direct data anchor citation from the log (e.g., "[Match ID #104 - Jett - Ascent]"). If you cannot anchor it, do not include it.

DIRECTIONS:
1. PERFORMANCE DROPS: Identify patterns where performance metrics significantly dip. Look strictly for correlations between high death rates, specific agent roles, or low KAST % present in the logs.
2. PEAK PERFORMANCE: Identify patterns where performance is exceptionally high. Identify the specific agents, maps, first-blood success rates, or economy states driving these wins based purely on the data.

OUTPUT FORMAT REQUIREMENTS:
- Use clear, scannable bullet points.
- Do NOT give generic Valorant advice (e.g., "work on crosshair placement" or "use voice comms"). Every piece of advice must be hyper-precise, compact, and highly impactful based on the logs.
- Explain the underlying "why" (tactical and positioning logic) behind the verified pattern.
- Maintain a highly supportive, positive, and constructive coaching tone.

<MATCH_HISTORY_DATA>
{parsed_match}
</MATCH_HISTORY_DATA>
"""
    result = client.chat.completions.create(model=GROQ_MODEL,messages=[{"role": "user", "content": prompt}])
    return(result.choices[0].message.content)

if __name__ == "__main__":
    advice = get_coaching("Eclipse", "5949")
    print(advice)