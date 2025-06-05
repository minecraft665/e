import fetch from "node-fetch";

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  const { message } = req.body;

  // Groq API Key ve URL
  const GROQ_API_KEY = "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";
  const GROQ_API_URL = "https://api.groq.com/v1/chat/completions";

  const response = await fetch(GROQ_API_URL, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${GROQ_API_KEY}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      model: "mixtral-8x7b-32768",
      messages: [{ role: "user", content: message }],
      temperature: 0.7
    })
  });

  const data = await response.json();
  const reply = data.choices[0].message.content;

  res.status(200).json({ reply });
}
