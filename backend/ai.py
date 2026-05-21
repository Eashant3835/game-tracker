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
    prompt = f"You are an AI valorant coach. Your job is to help the user play at their best level and you will do that by analyzing {parsed_match} and you should stay 100% faithful to this data at all times, which is the match history. You will look for patterns where the user's performance is dropping or less consistent and patterns where the user is performing really good and more consistent. Use these patterns to guide the user into playing better with better stats. You will provide this information in bullet point forms, while also breifly explaining your reasons and the matches you pulled them from.  Make advices precise compact and impactful and maintain a supportive positive tone"
    result = client.chat.completions.create(model=GROQ_MODEL,messages=[{"role": "user", "content": prompt}])
    return(result.choices[0].message.content)

if __name__ == "__main__":
    advice = get_coaching("Eclipse", "5949")
    print(advice)