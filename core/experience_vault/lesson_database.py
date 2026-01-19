import sqlite3
import os
from datetime import datetime

class ExperienceVault:
    def __init__(self, db_path="vault/experience.db"):
        os.makedirs("vault", exist_ok=True)
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """إنشاء الجداول إذا لم تكن موجودة"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS lessons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                game_title TEXT,
                genre TEXT,
                mechanics TEXT,
                code_snippet TEXT,
                lesson_learned TEXT,
                timestamp DATETIME
            )
        ''')
        conn.commit()
        conn.close()

    def store_experience(self, game_title, genre, mechanics, code, lesson):
        """حفظ خبرة جديدة في الخزنة"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO lessons (game_title, genre, mechanics, code_snippet, lesson_learned, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (game_title, genre, str(mechanics), code, lesson, datetime.now()))
        conn.commit()
        conn.close()
        return "✅ تم حفظ الخبرة في الخزنة السيادية."

    def get_all_experiences(self):
        """استرجاع كل ما تعلمه المصنع"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM lessons ORDER BY timestamp DESC')
        rows = cursor.fetchall()
        conn.close()
        return rows

