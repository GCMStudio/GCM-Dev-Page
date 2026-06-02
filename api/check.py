import json
from pathlib import Path

def handler(request):
    try:
        body = request.get_json() or {}
        current_version = body.get("version", "0.0.0")

        with open(
            Path(__file__).parent.parent / "versions.json",
            encoding="utf-8"
        ) as f:
            config = json.load(f)

        latest = config["latest"]

        return {
            "statusCode": 200,
            "body": {
                "currentVersion": current_version,
                "latestVersion": latest,
                "needsUpdate": current_version != latest,

                # Download
                "downloadUrl": config["downloadUrl"],

                # Informações extras
                "minimumVersion": config.get("minimumVersion"),
                "releaseDate": config.get("releaseDate"),
                "build": config.get("build", 0),
                "changelog": config.get("changelog", [])
            }
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": {
                "error": str(e)
            }
        }
