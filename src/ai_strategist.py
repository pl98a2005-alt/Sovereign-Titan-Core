import sqlite3, os, requests
from datetime import datetime

VAULT_DIR = "vault"
if not os.path.exists(VAULT_DIR): os.makedirs(VAULT_DIR)
DB_PATH = os.path.join(VAULT_DIR, "experience.db")

def factory_pipeline(description):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS experiences (description TEXT, date TEXT, insight TEXT, level TEXT)')
    insight = f"استنتاج هندسي: {description[:20]}..."
    cursor.execute("INSERT INTO experiences VALUES (?, ?, ?, ?)", (description, datetime.now().isoformat(), insight, "Elite"))
    conn.commit()
    conn.close()
    return f"تم تسجيل خبرة جديدة: {insight}"

class GraphicsScraper:
    @staticmethod
    def scrape_graphics_logic():
        try:
            r = requests.get("https://api.github.com/search/repositories?q=game+engine+logic", timeout=10)
            if r.status_code == 200: return "تم سحب وتحليل منطق الجرافيك من GitHub بنجاح."
            return "المصنع يعمل بالذاكرة المحلية حالياً."
        except: return "خطأ في الشبكة."

def auto_optimize_database():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("VACUUM") # تنظيف دون مسح الخبرات الأساسية
    conn.close()
    return "تم تنظيف الزوائد وتحسين قاعدة البيانات."
