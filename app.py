from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pathlib import Path
from chatbot import get_ai_response
from database import init_db, save_message, get_history

app=Flask(__name__); CORS(app); init_db()
FRONTEND=Path(__file__).resolve().parent.parent/"frontend"

@app.route("/")
def home(): return send_from_directory(FRONTEND,"index.html")

@app.route("/<path:filename>")
def files(filename): return send_from_directory(FRONTEND,filename)

@app.post("/api/chat")
def chat():
    try:
        data=request.get_json(silent=True) or {}
        msg=str(data.get("message","")).strip()
        conv=data.get("conversation",[])
        if not msg: return jsonify({"error":"Message cannot be empty"}),400
        reply=get_ai_response(msg,conv)
        save_message("user",msg); save_message("bot",reply)
        return jsonify({"reply":reply})
    except Exception as e:
        return jsonify({"error":str(e)}),500

@app.get("/api/health")
def health(): return jsonify({"status":"online","ai":"Ollama"})

if __name__=="__main__": app.run(host="127.0.0.1",port=5000,debug=True)
