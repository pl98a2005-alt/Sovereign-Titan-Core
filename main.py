import os
import json

def autonomous_engine():
    print("👑 Sovereign Titan v21: Logic Check...")
    
    # تأمين المسارات
    os.makedirs("games", exist_ok=True)
    os.makedirs("concepts", exist_ok=True)

    # بيانات استنتاجية (بدلاً من Ollama المتعثر)
    game_data = {
        "title": "Titan_Quest_v1",
        "genre": "Open World Survival",
        "mechanics": ["Resource Gathering", "Base Building", "AI Hunting"]
    }

    # حفظ المفهوم
    with open("concepts/last_build.json", "w") as f:
        json.dump(game_data, f)

    # توليد كود اللعبة
    project_path = f"games/{game_data['title']}"
    os.makedirs(project_path, exist_ok=True)
    
    game_code = f"""
from tkinter import messagebox
import time

def start_game():
    print("Welcome to {game_data['title']}")
    print("Genre: {game_data['genre']}")
    print("Core Mechanics: {', '.join(game_data['mechanics'])}")

if __name__ == '__main__':
    start_game()
"""
    with open(f"{project_path}/main.py", "w") as f:
        f.write(game_code)
    
    print(f"✅ Success! Game '{game_data['title']}' generated in /games folder.")

if __name__ == "__main__":
    autonomous_engine()
