import os
import json
from datetime import datetime

# ==========================
# Config
# ==========================

HISTORY_FOLDER = "chat_history"
HISTORY_FILE = os.path.join(HISTORY_FOLDER, "history.json")


# ==========================
# Load History
# ==========================

def load_history():

    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception:
        return []

# ==========================
# Save History
# ==========================

def save_history(history):

    os.makedirs(HISTORY_FOLDER, exist_ok=True)

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:

        json.dump(
            history,
            f,
            indent=4,
            ensure_ascii=False
        )


# ==========================
# Save Chat
# ==========================

def save_chat(pdf_name, messages):

    history = load_history()

    title = "New Chat"

    for msg in messages:

        if msg["role"] == "user":

            title = msg["content"][:50]

            break

    history.insert(
        0,
        {
            "id": str(datetime.now().timestamp()),
            "title": title,
            "pdf": pdf_name,
            "messages": messages,
            "time": datetime.now().strftime("%d-%m-%Y %H:%M")
        }
    )

    save_history(history)


# ==========================
# Delete Chat
# ==========================

def delete_chat(chat_id):

    history = load_history()

    history = [
        chat
        for chat in history
        if chat["id"] != chat_id
    ]

    save_history(history)


# ==========================
# Rename Chat
# ==========================

def rename_chat(chat_id, new_title):

    history = load_history()

    for chat in history:

        if chat["id"] == chat_id:

            chat["title"] = new_title

            break

    save_history(history)