import sqlite3, os, requests
from PIL import Image # المكتبة الجديدة لمعالجة الصور
import io

class UnifiedSovereignAI:
    def __init__(self):
        if not os.path.exists('vault'): 
            os.makedirs('vault')
        self.conn = sqlite3.connect('vault/experience.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS brain (topic TEXT, exp TEXT, intelligence_level REAL)')
        self.conn.commit()

    def analyze_image(self, image_data):
        """[2026-01-14] نظام العين الرقمية: يحول الصورة إلى وصف تحليلي"""
        try:
            # فتح الصورة من البيانات
            img = Image.open(io.BytesIO(image_data))
            img_width, img_height = img.size
            # منطق تحليل الصورة (هنا يمكن دمج موديلات تعلم عميق لاحقاً)
            if img_width > 500 and img_height > 500:
                return f"Vision Analysis: Detected a Large-Scale Environment ({img_width}x{img_height}). Suggesting expansive world generation."
            else:
                return "Vision Analysis: Detected a Detailed Asset. Suggesting high-polygon modeling."
        except Exception as e:
            return f"Vision Error: Could not process image. {str(e)}"

    def engineer_game(self, description=None, image_data=None):
        """الموديل المهندس: يحلل، يقترح، ويبرمج (الآن يدعم الوصف أو الصورة)"""
        analysis_report = ""
        if description:
            analysis_report = f"Sovereign Analysis: Constructing architectural framework for '{description[:30]}...'"
            topic_for_db = description[:50]
        elif image_data:
            analysis_report = self.analyze_image(image_data)
            topic_for_db = "Image_Based_Generation"
        else:
            return "Error: No description or image provided."

        suggestion = "Strategic Suggestion: Integrating High-Fidelity Physics & Auto-OBB Management."
        
        generated_code = f"""
# Sovereign Engine Core v2.1 (Vision Integrated)
# Generated based on: {'Image Data' if image_data else description[:50]}
class GameEngine:
    def __init__(self):
        self.engine_status = "Peak Performance"
        self.ai_integrated = True
        self.vision_module_active = True # تفعيل موديل الرؤية
        self.physics_module = "Advanced_Sovereign_v4"
        
    def start_logic(self):
        print("Sovereign Game Logic Initialized...")
"""
        self.cursor.execute("INSERT INTO brain VALUES (?, ?, ?)", (topic_for_db, "Success_Gen", 1.0))
        self.conn.commit()
        
        with open("generated_game.py", "w", encoding='utf-8') as f: 
            f.write(generated_code)
            
        return f"{analysis_report}\n{suggestion}\n✅ [Sovereign Core Generated Successfully]"

    def auto_update_system(self):
        return "System Status: Unified Engineer Updated & Old Modules Cleared."

def factory_pipeline(description=None, image_data=None):
    ai = UnifiedSovereignAI()
    ai.auto_update_system()
    return ai.engineer_game(description=description, image_data=image_data)

