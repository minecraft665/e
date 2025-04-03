from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

# Groq API konfigürasyonu
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")
client = Groq(api_key=GROQ_API_KEY)
MODEL_NAME = "llama3-70b-8192"  # Güncel model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({"error": "Boş mesaj gönderilemez"}), 400
        
        # Groq API'den yanıt al
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": user_message}],
            model=MODEL_NAME,
            temperature=0.7,
            max_tokens=1024
        )
        
        ai_response = response.choices[0].message.content
        
        return jsonify({
            "user_message": user_message,
            "ai_response": ai_response
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5001)
