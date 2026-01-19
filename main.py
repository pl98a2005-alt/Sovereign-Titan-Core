import os
import sqlite3
from datetime import datetime

class SovereignKernel:
    def __init__(self):
        print("--- [ Sovereign Titan V3: Initialization ] ---")
        self.setup_environment()
        self.init_brain()

    def setup_environment(self):
        """إنشاء المجلدات الأساسية للمصنع"""
        folders = ['kernel', 'factory', 'brain', 'production', 'assets']
        for folder in folders:
            if not os.path.exists(folder):
                os.makedirs(folder)
                print(f"✅ تم إنشاء مجلد: {folder}")

    def init_brain(self):
        """تأسيس خزنة الخبرة (التعلم الذاتي)"""
        self.conn = sqlite3.connect('brain/experience.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_name TEXT,
                result TEXT,
                timestamp DATETIME
            )
        ''')
        self.conn.commit()
        print("✅ خزنة الخبرة جاهزة للتعلم.")

    def log_experience(self, task, status):
        """تسجيل كل حركة يقوم بها المصنع"""
        self.cursor.execute("INSERT INTO history (task_name, result, timestamp) VALUES (?, ?, ?)",
                           (task, status, datetime.now()))
        self.conn.commit()

# تشغيل النواة لأول مرة
if __name__ == "__main__":
    titan = SovereignKernel()
    titan.log_experience("System Startup", "Success")
    print("--- [ المصنع الآن في وضع الاستعداد التام ] ---")
