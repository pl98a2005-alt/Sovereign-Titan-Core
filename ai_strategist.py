import sqlite3

class AIStrategist:
    def __init__(self):
        # إنشاء قاعدة بيانات الخبرات التراكمية
        self.conn = sqlite3.connect('vault/experience.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS knowledge 
                               (genre TEXT, pattern TEXT, quality_score REAL)''')
        self.conn.commit()

    def analyze_genre(self, user_description):
        # منطق الوعي: تحليل الكلمات المفتاحية لتحديد نوع اللعبة
        desc = user_description.lower()
        if "حرب" in desc or "قتال" in desc:
            return "WAR_GENRE"
        elif "سيارات" in desc or "سباق" in desc:
            return "RACING_GENRE"
        return "UNKNOWN_MEGA_PROJECT"

    def suggest_improvements(self, genre):
        # اقتراحات ذكية لسد النواقص
        suggestions = {
            "WAR_GENRE": "أقترح دمج نظام فيزياء المقذوفات وتحسين ملفات الـ OBB للخرائط.",
            "RACING_GENRE": "نقص مرصود: فيزياء الاحتكاك. أقترح إضافة محرك رندرة للإطارات."
        }
        return suggestions.get(genre, "أقترح تحليل هياكل الألعاب العالمية لزيادة الضخامة.")

