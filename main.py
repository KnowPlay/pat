from flask import Flask, request, jsonify

app = Flask(__name__)

# ROUTES
@app.route("/")
def home():
    return "Welcome to the MLB Team API!"

# GET
# path param
@app.route("/get-team/<team_id>")
def get_team(team_id):
    # create a dict
    team_data = [
        {"team_id": "ARI", "name": "Arizona Diamondbacks", "website": "dbacks.com"},
        {"team_id": "ATL", "name": "Atlanta Braves", "website": "braves.com"},
        {"team_id": "BAL", "name": "Baltimore Orioles", "website": "orioles.com"},
        {"team_id": "BOS", "name": "Boston Red Sox", "website": "redsox.com"},
        {"team_id": "CHC", "name": "Chicago Cubs", "website": "cubs.com"},
        {"team_id": "CWS", "name": "Chicago White Sox", "website": "whitesox.com"},
        {"team_id": "CIN", "name": "Cincinnati Reds", "website": "reds.com"},
        {"team_id": "CLE", "name": "Cleveland Guardians", "website": "cleguardians.com"},
        {"team_id": "COL", "name": "Colorado Rockies", "website": "rockies.com"},
        {"team_id": "DET", "name": "Detroit Tigers", "website": "tigers.com"},
        {"team_id": "HOU", "name": "Houston Astros", "website": "astros.com"},
        {"team_id": "KC", "name": "Kansas City Royals", "website": "royals.com"},
        {"team_id": "LAA", "name": "Los Angeles Angels", "website": "angels.com"},
        {"team_id": "LAD", "name": "Los Angeles Dodgers", "website": "dodgers.com"},
        {"team_id": "MIA", "name": "Miami Marlins", "website": "marlins.com"},
        {"team_id": "MIL", "name": "Milwaukee Brewers", "website": "brewers.com"},
        {"team_id": "MIN", "name": "Minnesota Twins", "website": "twins.com"},
        {"team_id": "NYM", "name": "New York Mets", "website": "mets.com"},
        {"team_id": "NYY", "name": "New York Yankees", "website": "yankees.com"},
        {"team_id": "OAK", "name": "Oakland Athletics", "website": "athletics.com"},
        {"team_id": "PHI", "name": "Philadelphia Phillies", "website": "phillies.com"},
        {"team_id": "PIT", "name": "Pittsburgh Pirates", "website": "pirates.com"},
        {"team_id": "SD", "name": "San Diego Padres", "website": "padres.com"},
        {"team_id": "SF", "name": "San Francisco Giants", "website": "sfgiants.com"},
        {"team_id": "SEA", "name": "Seattle Mariners", "website": "mariners.com"},
        {"team_id": "STL", "name": "St. Louis Cardinals", "website": "cardinals.com"},
        {"team_id": "TB", "name": "Tampa Bay Rays", "website": "raysbaseball.com"},
        {"team_id": "TEX", "name": "Texas Rangers", "website": "texasrangers.com"},
        {"team_id": "TOR", "name": "Toronto Blue Jays", "website": "bluejays.com"},
        {"team_id": "WSH", "name": "Washington Nationals", "website": "nationals.com"}
    ]
    
    if team_data:
        return jsonify(team_data), 200
    else:
        return jsonify({"error": "Team not found"}), 404
    
    
# POST
# specify methods
@app.route("/create-team", methods=["POST"])
def create_team():
    if request.method == "POST":
        user_data = request.get_json()
        
        return jsonify(user_data), 201
    else:
        return jsonify({"error": "Team not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)