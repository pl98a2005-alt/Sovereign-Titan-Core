import asyncio
from core.cognitive_engine.concept_analyzer import analyze_game_concept
from core.code_generator.architecture_builder import ArchitectureBuilder

async def start():
    print("🚀 Starting Sovereign Titan Factory...")
    description = "لعبة حرب عصابات في شوارع بغداد، منظور ثالث، تركز على التخفي"
    
    # 1. تحليل
    concept, path = await analyze_game_concept(description)
    print(f"🧠 AI analyzed: {concept.get('game_title')}")
    
    # 2. تصنيع
    builder = ArchitectureBuilder(path)
    result = builder.create_game_files()
    print(result)

if __name__ == "__main__":
    asyncio.run(start())

