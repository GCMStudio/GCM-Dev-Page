import json
from pathlib import Path

def handler(request):
    try:
        body = request.get_json() or {}
        current_version = body.get("version", "0.0.0")

        with open(
            Path(__file__).parent / "versions.json",
            encoding="utf-8"
        ) as f:
            config = json.load(f)

        latest = config["latest"]
        latest_info = config["versions"][latest]

        return {
            "statusCode": 200,
            "body": {
                "currentVersion": current_version,
                "latestVersion": latest,
                "needsUpdate": current_version != latest,

                "downloadUrl": latest_info["downloadUrl"],
                "minimumVersion": latest_info["minimumVersion"],
                "releaseDate": latest_info["releaseDate"],
                "build": latest_info["build"],
                "changelog": latest_info["changelog"]
            }
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": {
                "error": str(e)
            }
        }
