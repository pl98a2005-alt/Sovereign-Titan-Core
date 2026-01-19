import asyncio
from core.cognitive_engine.concept_analyzer import analyze_game_concept
from core.code_generator.architecture_builder import ArchitectureBuilder
from core.learning_engine.market_researcher import MarketResearcher
from core.experience_vault.lesson_database import ExperienceVault

async def run_sovereign_cycle():
    print("🛰️ Sovereign Titan v21: Research & Production Cycle Started.")
    
    # 1. البحث في الإنترنت (التعلم من السوق)
    researcher = MarketResearcher()
    trends = researcher.research_trends()
    
    # 2. إرسال التريندات للـ AI لتصميم لعبة "تكتسح السوق"
    description = f"أريد لعبة أندرويد تجمع بين تريندات اليوم: {', '.join(trends)}"
    print(f"🧠 AI is designing a game based on market trends...")
    
    concept, path = await analyze_game_concept(description)
    
    # 3. بناء الكود وحفظ الخبرة
    builder = ArchitectureBuilder(path)
    builder.create_game_files()
    
    vault = ExperienceVault()
    vault.store_experience(
        game_title=concept.get('game_title'),
        genre=concept.get('genre'),
        mechanics=concept.get('mechanics'),
        code="Trend-Based Logic",
        lesson=f"Market research integrated: {trends[0]} is dominating."
    )
    
    print(f"👑 Mission Accomplished: {concept.get('game_title')} is ready.")

if __name__ == "__main__":
    asyncio.run(run_sovereign_cycle())
