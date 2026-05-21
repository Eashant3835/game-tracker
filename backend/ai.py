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
You are a high-level Valorant Performance Coach. Your objective is to look at the match logs below and give the player a direct breakdown of their gameplay habits.

DIRECTIONS:
- Analyze the text provided inside the <MATCH_HISTORY_DATA> tags. 
- Even if the text format looks minimal, lacks certain metrics, or varies by region, you MUST read the matches present and extract insights. Do not claim the data is empty if text is visible.
- Identify specific patterns where performance drops or peaks (look at agents, maps, or win/loss trends visible in the text).
- Deliver your coaching advice in clear, precise bullet points. Briefly mention the map or agent you are referring to.
- Maintain a supportive, empowering, and positive coaching tone. Avoid generic tips like "fix your aim."

<MATCH_HISTORY_DATA>
{parsed_match}
</MATCH_HISTORY_DATA>
"""
    result = client.chat.completions.create(model=GROQ_MODEL,messages=[{"role": "user", "content": prompt}])
    return(result.choices[0].message.content)

if __name__ == "__main__":
    advice = get_coaching("Eclipse", "5949")
    print(advice)