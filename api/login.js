// api/login.js

export default function handler(req, res) {

    if (req.method !== "POST") {
        return res.status(405).json({
            message: "Método não permitido"
        });
    }

    const { username, password } = req.body;

    if (username === "admin" && password === "21012014Gu*") {
        return res.status(200).json({
            status: "valido",
            message: "Login válido"
        });
    }

    return res.status(401).json({
        status: "invalido",
        message: "Login inválido"
    });
}
