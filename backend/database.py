import sqlite3

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
        
if __name__ == "__main__":
    init_db()