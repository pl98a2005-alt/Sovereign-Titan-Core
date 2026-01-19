import json, asyncio, aiohttp, os
from datetime import datetime

class ConceptAnalyzer:
    def __init__(self):
        self.ollama_url = "http://localhost:11434/api/generate"
        self.model = "llama3:8b"

    async def analyze_concept(self, description):
        prompt = f"Analyze this game concept and return ONLY JSON: {description}"
        payload = {"model": self.model, "prompt": prompt, "stream": False}
        
        async with aiohttp.ClientSession() as session:
            async with session.post(self.ollama_url, json=payload) as resp:
                data = await resp.json()
                raw_json = data.get('response', '{}')
                # تنظيف النص ليصبح JSON صالح
                start = raw_json.find('{')
                end = raw_json.rfind('}') + 1
                concept_data = json.loads(raw_json[start:end])
                
                # حفظ النتيجة
                os.makedirs("concepts", exist_ok=True)
                filepath = f"concepts/game_{datetime.now().strftime('%H%M%S')}.json"
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(concept_data, f, ensure_ascii=False, indent=2)
                return concept_data, filepath

async def analyze_game_concept(description):
    analyzer = ConceptAnalyzer()
    return await analyzer.analyze_concept(description)

