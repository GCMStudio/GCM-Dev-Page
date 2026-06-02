from flask import Flask, request, jsonify
import json
from pathlib import Path

app = Flask(__name__)

@app.route("/api/check", methods=["POST"])
def check():
    body = request.get_json() or {}
    current_version = body.get("version", "0.0.0")

    with open(
        Path(__file__).parent / "versions.json",
        encoding="utf-8"
    ) as f:
        config = json.load(f)

    latest = config["latest"]
    latest_info = config["versions"][latest]

    return jsonify({
        "currentVersion": current_version,
        "latestVersion": latest,
        "needsUpdate": current_version != latest,
        "downloadUrl": latest_info["downloadUrl"],
        "minimumVersion": latest_info["minimumVersion"],
        "releaseDate": latest_info["releaseDate"],
        "build": latest_info["build"],
        "changelog": latest_info["changelog"]
    })
app = app
