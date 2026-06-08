const fs = require("fs");
const path = require("path");

module.exports = (req, res) => {
    try {
        const currentVersion = req.body?.version || "0.0.0";

        const config = JSON.parse(
            fs.readFileSync(
                path.join(__dirname, "versions.json"),
                "utf8"
            )
        );

        const latest = config.latest;
        const latestInfo = config.versions[latest];

        res.status(200).json({
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
        res.status(500).json({
            error: err.message
        });
    }
};
