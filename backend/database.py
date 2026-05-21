import sqlite3
from valorant_api import get_puuid, parse_match_stats

def init_db():
    with sqlite3.connect("data.db") as conn:
        #cursors are how you interract with DB
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                tag TEXT,
                region TEXT,
                puuid TEXT,
                last_searched TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS matches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_id INTEGER,
                map TEXT,
                agent TEXT,
                kills INTEGER,
                deaths INTEGER,
                assists INTEGER,
                headshots INTEGER,
                bodyshots INTEGER,
                legshots INTEGER,
                damage_dealt INTEGER,
                damage_taken INTEGER,
                match_outcome TEXT,
                Q INTEGER,
                C INTEGER,
                E INTEGER,
                X INTEGER
            )
        """)

def save_player(name,tag,region,puuid):
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM players WHERE name = ? AND tag = ?", (name, tag))
        existing = cursor.fetchone()
        if existing:
            return existing[0]
        else:
            cursor.execute(
                "INSERT INTO players (name, tag, region, puuid) VALUES (?,?,?,?)", (name,tag,region,puuid)
            )
            return(cursor.lastrowid)


def save_matches(player_id, matches):
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        for match in matches:
            cursor.execute(
            "INSERT INTO matches (player_id, map, agent, kills, deaths, assists, headshots, bodyshots, legshots, Q, C, E, X, match_outcome, damage_dealt, damage_taken) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(player_id, match['map'], match['agent'], match['kills'], match['deaths'], match['assists'], match['headshots'], match['bodyshots'], match['legshots'], match['Q'], match['C'], match['E'], match['X'], match['match_outcome'], match['damage_dealt'], match['damage_taken'])
            )

if __name__ == "__main__":
    init_db()
    puuid = get_puuid("Eclipse","5949")
    player_id = save_player("Eclipse", "5949", "na", puuid)
    matches = parse_match_stats("Eclipse", "5949")
    save_matches(player_id,matches)