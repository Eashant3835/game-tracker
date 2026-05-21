from flask import Flask, jsonify, request
from database import init_db
from valorant_api import get_puuid, parse_match_stats
from ai import get_coaching
from database import save_matches, save_player
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")
init_db()

@app.route("/search")
def search():
    try:
        name = request.args.get("name")
        tag = request.args.get("tag")
        region = request.args.get("region")
        puuid = get_puuid(name, tag)
        player_id = save_player(name,tag,region,puuid)
        matches = parse_match_stats(name, tag)
        save_matches(player_id,matches)
        coaching = get_coaching(name, tag)
        return jsonify({"matches":matches,"coaching":coaching})
    except Exception as e:
        print(e)
        return(jsonify({"error": str(e)}), 500)

if __name__ == "__main__":
    app.run(debug=True)

