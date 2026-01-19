import asyncio
from core.cognitive_engine.concept_analyzer import analyze_game_concept
from core.code_generator.architecture_builder import ArchitectureBuilder
from core.experience_vault.lesson_database import ExperienceVault
from utils.cleaner import factory_clean_up

async def run_factory():
    # 1. تهيئة الخزنة
    vault = ExperienceVault()
    
    # 2. تشغيل المصنع
    description = "لعبة بقاء في غابة موحشة للأندرويد"
    concept, path = await analyze_game_concept(description)
    
    # 3. بناء الكود
    builder = ArchitectureBuilder(path)
    msg = builder.create_game_files()
    print(msg)
    
    # 4. حفظ التجربة في الخزنة (التعلم الذاتي)
    vault.store_experience(
        game_title=concept.get('game_title'),
        genre=concept.get('genre'),
        mechanics=concept.get('mechanics'),
        code="Main KivyMD Layout",
        lesson="Successfully integrated localized AI logic for mobile"
    )
    
    # 5. تنظيف النظام (بناءً على طلبك)
    # يمكنك استدعاء factory_clean_up() هنا أو عند الحاجة
    print("🚀 Cycle finished. Sovereign Titan is getting smarter.")

if __name__ == "__main__":
    asyncio.run(run_factory())
