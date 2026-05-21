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
    from valorant_api import parse_match_stats
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")

client = Groq(api_key=GROQ_API_KEY)

def get_coaching(name, tag, region):
    parsed_match = parse_match_stats(name, tag)
    
    # Pre-calculations
    total_matches = len(parsed_match)
    wins = sum(1 for m in parsed_match if m["match_outcome"] == "Win")
    avg_kills = sum(m["kills"] for m in parsed_match) / total_matches
    avg_deaths = sum(m["deaths"] for m in parsed_match) / total_matches
    avg_damage = sum(m["damage_dealt"] for m in parsed_match) / total_matches
    avg_hs = sum(m["headshots"] for m in parsed_match) / total_matches
    avg_shots = sum(m["headshots"] + m["bodyshots"] + m["legshots"] for m in parsed_match) / total_matches
    hs_pct = (avg_hs / avg_shots * 100) if avg_shots > 0 else 0
    avg_eco = sum(m["economy_spent"] for m in parsed_match) / total_matches
    avg_kd = avg_kills / avg_deaths if avg_deaths > 0 else avg_kills

    prompt = f"""You are a Valorant coach analyzing a player's last {total_matches} matches.

PLAYER STATS SUMMARY:
- Win rate: {wins}/{total_matches} ({wins/total_matches*100:.0f}%)
- Avg KD: {avg_kd:.2f}
- Avg kills: {avg_kills:.1f} | Avg deaths: {avg_deaths:.1f}
- Avg damage per match: {avg_damage:.0f}
- Headshot %: {hs_pct:.1f}%
- Avg economy spent: {avg_eco:.0f}

MATCH BY MATCH DATA:
{parsed_match}

    INSTRUCTIONS:
    Address the user directly as "you" — never refer to them as "the player".
    Be a coach talking to your athlete, not an analyst writing a report.
    Maximum 5 bullet points, one sentence each. Be ruthlessly concise.
    Reference specific matches by map and agent (e.g. "your Jett game on Ascent") never as "Match 1" or "Match X".
    Every point must include a specific number from the data. No generic advice.
    If economy_spent is 0 or under 100, ignore that match for economy analysis as the data is likely missing.
    Analyze: consistency, aim, economy, agent impact, and one thing you're doing well."""

    result = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return result.choices[0].message.content


if __name__ == "__main__":
    advice = get_coaching("Eclipse", "5949")
    print(advice)