import requests
OLLAMA_URL="http://127.0.0.1:11434/api/chat"
MODEL="llama3.2"
SYSTEM="""You are PyBot, a helpful general-purpose AI assistant. Answer clearly and accurately. Help with programming, B.Tech subjects, mathematics, databases, networking, AI/ML, writing, debugging, general knowledge and everyday questions. Use simple explanations when useful. For code, provide complete code and explain it. If unsure, say so."""
def get_ai_response(message,conversation=None):
    messages=[{"role":"system","content":SYSTEM}]
    for x in (conversation or [])[-10:]:
        if x.get("role") in ("user","assistant") and x.get("content"):
            messages.append({"role":x["role"],"content":x["content"]})
    messages.append({"role":"user","content":message})
    r=requests.post(OLLAMA_URL,json={"model":MODEL,"messages":messages,"stream":False},timeout=180)
    r.raise_for_status()
    return r.json()["message"]["content"]
