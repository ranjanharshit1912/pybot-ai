import sqlite3
from pathlib import Path
DB=Path(__file__).resolve().parent/"chatbot.db"
def init_db():
    with sqlite3.connect(DB) as c:
        c.execute("CREATE TABLE IF NOT EXISTS messages(id INTEGER PRIMARY KEY AUTOINCREMENT,sender TEXT,message TEXT,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
def save_message(sender,message):
    with sqlite3.connect(DB) as c: c.execute("INSERT INTO messages(sender,message) VALUES(?,?)",(sender,message))
def get_history():
    with sqlite3.connect(DB) as c: rows=c.execute("SELECT sender,message,created_at FROM messages ORDER BY id").fetchall()
    return [{"sender":r[0],"message":r[1],"created_at":r[2]} for r in rows]
