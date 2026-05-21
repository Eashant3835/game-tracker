import os
from dotenv import load_dotenv
import requests
import json

#Get the API key from env file
load_dotenv()
HENRIK_API_KEY = os.getenv("HENRIK_API_KEY")


#Getting the player's puuid
def get_puuid(name,tag):
    try:
        url = f"https://api.henrikdev.xyz/valorant/v2/account/{name}/{tag}"
        headers = {
            "Authorization": HENRIK_API_KEY
        } #Got url from documentation, header is to authenticate

        response = requests.get(url,headers=headers)
        account_details = response.json() #json to dict
        puuid = account_details.get("data", {}) .get("puuid") #Grab puuid from data dict "{}" is a failsafe
        return(puuid)
    
    except requests.exceptions.RequestException: 
        print("Request failed, Please try again!")
        return(None)
    
#Getting the match history of the player
def get_matches(region,puuid):
    try:
        url = f"https://api.henrikdev.xyz/valorant/v3/by-puuid/matches/{region}/{puuid}?size=20"
        headers = {
            "Authorization": HENRIK_API_KEY
        }#Got url from documentation, header is to authenticate
        response = requests.get(url,headers=headers)
        match_history = response.json() #json to dict
        return(match_history)
    
    except requests.exceptions.RequestException:
        print("Request failed, Please try again!")
        return(None)
    
#Translating into a clean list with dicts
def parse_match_stats(name, tag):
    puuid = get_puuid("Eclipse",5949)
    result = get_matches("na",puuid)
    parsed_matches = []
    for match in result["data"]:
        for player in match["players"]["all_players"]:
            if player["name"] == name and player["tag"] == tag: #Searching only for our player's stats
                stats = player["stats"]
                ability_casts = player["ability_casts"]
                player_team = player["team"]
                if match["teams"][player_team.lower()]["has_won"] == True:
                    match_result = "Win"
                else:
                    match_result = "Loss"
                match_summary = {
                    "map":match["metadata"]["map"],
                    "agent":player['character'],
                    "kills":stats['kills'],
                    "deaths":stats['deaths'],
                    "assists":stats['assists'],
                    "headshots":stats['headshots'],
                    "bodyshots":stats['bodyshots'],
                    "legshots":stats['legshots'],
                    "Q":ability_casts['q_cast'],
                    "C":ability_casts['c_cast'],
                    "E":ability_casts['e_cast'],
                    "X":ability_casts['x_cast'],
                    "match_outcome":match_result,
                    "damage_dealt":player["damage_made"],
                    "damage_taken":player["damage_received"]                                                               
                }
                parsed_matches.append(match_summary)
    return(parsed_matches)
    