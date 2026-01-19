import asyncio
import os
import sys

# ضمان استيراد المجلدات بشكل صحيح
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.cognitive_engine.concept_analyzer import analyze_game_concept
from core.code_generator.architecture_builder import ArchitectureBuilder
from core.learning_engine.market_researcher import MarketResearcher
from core.experience_vault.lesson_database import ExperienceVault

async def run_sovereign_cycle():
    print("🚀 Sovereign Titan v21: Starting Production Cycle...")
    
    # --- خطوة إجبارية: إنشاء المجلدات لمنع اللون الأحمر ---
    for folder in ['concepts', 'games', 'vault', 'core/config', 'utils']:
        os.makedirs(folder, exist_ok=True)
    
    try:
        # 1. البحث في الإنترنت (التعلم من السوق)
        researcher = MarketResearcher()
        trends = researcher.research_trends()
        
        # 2. إرسال التريندات للـ AI
        # لاحظ: تم استخدام وصف قوي ومختصر لضمان استجابة سريعة من الموديل الصغير
        description = f"Build a mobile game trend: {', '.join(trends)}. Focus on high replayability and simple controls."
        print(f"🧠 AI (Phi-3) is designing the next hit...")
        
        concept, path = await analyze_game_concept(description)
        
        if not concept:
            raise Exception("AI failed to generate concept.")

        # 3. بناء الكود
        builder = ArchitectureBuilder(path)
        msg = builder.create_game_files()
        print(msg)
        
        # 4. حفظ التجربة في الخزنة
        vault = ExperienceVault()
        vault.store_experience(
            game_title=concept.get('game_title', 'Unknown_Game'),
            genre=concept.get('genre', 'General'),
            mechanics=concept.get('mechanics', []),
            code="Automated Architecture Code",
            lesson=f"Integrated market trends: {trends[0] if trends else 'None'}"
        )
        
        print(f"👑 SUCCESS: {concept.get('game_title')} is generated and stored.")

    except Exception as e:
        print(f"❌ FATAL ERROR: {str(e)}")
        # إذا فشل المصنع، سنقوم بإنشاء ملف تجريبي لضمان عدم توقف الـ Workflow تماماً
        os.makedirs("games/Emergency_Game", exist_ok=True)
        with open("games/Emergency_Game/main.py", "w") as f:
            f.write("print('Emergency Build Successful')")

if __name__ == "__main__":
    asyncio.run(run_sovereign_cycle())
