import os, sys, threading, sqlite3, json, random, time
from datetime import datetime
import requests
from bs4 import BeautifulSoup

from kivy.config import Config
Config.set('graphics', 'resizable', '0')

from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.progressbar import MDProgressBar

# --- إعدادات اللغة العربية ---
try:
    from arabic_reshaper import reshape
    from bidi.algorithm import get_display
    def ar(t): return get_display(reshape(str(t)))
except:
    def ar(t): return str(t)

# --- النواة الذكية (التعلم والبحث) ---
class SovereignBrain:
    def __init__(self):
        self.db_path = "vault/experience.db"
        os.makedirs("vault", exist_ok=True)
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute('''CREATE TABLE IF NOT EXISTS experience 
                       (id INTEGER PRIMARY KEY, game_type TEXT, features TEXT, 
                        success_rate REAL, timestamp TEXT)''')
        conn.commit()

    def research_trends(self, query):
        """المصنع يبحث في الويب لفهم أنماط الألعاب"""
        try:
            # محاكاة بحث حقيقي (يمكن توسيعها بـ Scraper حقيقي)
            time.sleep(2)
            trends = {
                "mechanics": ["Bullet Drop", "Tactical Sprint", "Advanced Crafting"],
                "graphics": "PBR High-End",
                "security": "TitanGuard Anti-Cheat"
            }
            return trends
        except:
            return {"mechanics": ["Standard Physics"], "graphics": "Mobile Optimized"}

    def record_learning(self, game_type, features):
        conn = sqlite3.connect(self.db_path)
        conn.execute("INSERT INTO experience (game_type, features, success_rate, timestamp) VALUES (?,?,?,?)",
                     (game_type, json.dumps(features), 0.99, datetime.now().isoformat()))
        conn.commit()

# --- محرك التوزيع الهندسي (APK/OBB Engine) ---
class FactoryPipeline:
    def __init__(self):
        self.build_path = "build"
        os.makedirs(self.build_path, exist_ok=True)

    def engineer_game(self, game_id, specs):
        game_dir = f"{self.build_path}/{game_id}"
        os.makedirs(f"{game_dir}/APK", exist_ok=True)
        os.makedirs(f"{game_dir}/OBB", exist_ok=True)
        
        # إنشاء ملف APK وهمي (Structure)
        with open(f"{game_dir}/APK/launcher.apk", "w") as f:
            f.write(f"TITAN_EXE_{game_id}")
        
        # إنشاء ملف OBB وهمي
        with open(f"{game_dir}/OBB/main.100.{game_id}.obb", "wb") as f:
            f.write(os.urandom(1024 * 50)) 
        return game_dir

# --- الواجهة الرسومية ---
class TitanFactoryUI(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.brain = SovereignBrain()
        self.pipeline = FactoryPipeline()
        self.init_ui()

    def init_ui(self):
        self.add_widget(MDLabel(
            text=ar("مصنع سيوفيرن تايتان v20.0"),
            halign="center", pos_hint={"center_y": 0.9},
            font_style="H4", theme_text_color="Primary"
        ))

        self.input_desc = MDTextField(
            hint_text=ar("صف فكرة اللعبة هنا..."),
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            size_hint=(0.8, None)
        )
        self.add_widget(self.input_desc)

        self.progress = MDProgressBar(
            value=0, pos_hint={"center_y": 0.55}, size_hint_x=0.8, pos_hint_x=0.1
        )
        self.add_widget(self.progress)

        self.status = MDLabel(
            text=ar("🤖 بانتظار أوامر السيادة..."),
            halign="center", pos_hint={"center_y": 0.45},
            theme_text_color="Secondary"
        )
        self.add_widget(self.status)

        self.add_widget(MDFillRoundFlatButton(
            text=ar("🚀 بدء الإنتاج العبقري"),
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            on_release=self.start_production
        ))

    def start_production(self, instance):
        desc = self.input_desc.text
        if not desc: return
        threading.Thread(target=self.production_worker, args=(desc,), daemon=True).start()

    def production_worker(self, desc):
        Clock.schedule_once(lambda dt: setattr(self.status, 'text', ar("🌐 جاري تحليل السوق والتريندات العالمية...")))
        trends = self.brain.research_trends(desc)
        
        stages = [
            ("🧠 تم تحليل البيانات ووضع الخطة...", 30),
            ("🛠️ هندسة المعالج الرسومي والميكانيكيات...", 60),
            ("📦 توليد حزم APK و OBB المصنعة...", 90),
            ("✅ اكتمل الإنتاج العالمي!", 100)
        ]
        
        for msg, val in stages:
            time.sleep(1.5)
            Clock.schedule_once(lambda dt, m=msg, v=val: self.update_status(m, v))
        
        game_id = f"TITAN_{random.randint(1000,9999)}"
        self.pipeline.engineer_game(game_id, trends)
        self.brain.record_learning(desc, trends)

    def update_status(self, msg, val):
        self.status.text = ar(msg)
        self.progress.value = val

class SovereignTitanFactory(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        return TitanFactoryUI()

if __name__ == "__main__":
    SovereignTitanFactory().run()
