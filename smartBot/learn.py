# learn.py
import json

def learn_from_input(user_input):
    knowledge = load_memory()
    if user_input not in knowledge:
        knowledge[user_input] = "Učim, pitaj ponovo kasnije!"
        save_memory(knowledge)

def load_memory():
    try:
        with open("memory.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_memory(data):
    with open("memory.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
