import fs from "fs";
import path from "path";

export default function handler(req, res) {
    try {
        const currentVersion = req.body?.version || "0.0.0";

        const filePath = path.join(process.cwd(), "data", "versions.json");

        const config = JSON.parse(fs.readFileSync(filePath, "utf8"));

        const latest = config.latest;
        const latestInfo = config.versions[latest];

        return res.status(200).json({
            currentVersion,
            latestVersion: latest,
            needsUpdate: currentVersion !== latest,
            downloadUrl: latestInfo.downloadUrl,
            minimumVersion: latestInfo.minimumVersion,
            releaseDate: latestInfo.releaseDate,
            build: latestInfo.build,
            changelog: latestInfo.changelog
        });
    } catch (err) {
        return res.status(500).json({
            error: err.message
        });
    }
}
