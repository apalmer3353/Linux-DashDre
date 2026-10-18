from flask import Flask, jsonify, send_from_directory
import json

app = Flask(__name__)

# getting the latest stats from my monitoring agent
@app.route("/stats")
def stats():
    try:
        with open("/run/dashboard/latest.json", "r") as file:
            data = json.load(file)
        return jsonify(data)
    except (FileNotFoundError, json.JSONDecodeError):
        return jsonify({"error": "Stats are not available yet"}), 503

# showing my dashboard webpage
@app.route("/")
def dashboard():
    return send_from_directory(
        "/home/dre997005/linux-dashboard/dashboard",
        "index.html"
    )

@app.route("/history")
def history():
    readings = []

    try:
        with open("/home/dre997005/linux-dashboard/data/history.jsonl", "r") as file:
            for line in file:
                readings.append(json.loads(line))

        # most recent 60 
        return jsonify(readings[-60:])

    except FileNotFoundError:
        return jsonify([])

# starting the api on my server
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
