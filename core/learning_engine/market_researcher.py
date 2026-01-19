import requests
from bs4 import BeautifulSoup
import json

class MarketResearcher:
    def __init__(self):
        self.steam_url = "https://store.steampowered.com/search/?filter=topsellers"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def research_trends(self):
        """البحث عن أكثر الألعاب مبيعاً وتحليلها"""
        print("🔍 Searching the internet for latest gaming trends...")
        try:
            response = requests.get(self.steam_url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            trends = []
            # سحب أول 5 ألعاب تصدرت القائمة
            games = soup.find_all('span', class_='title')[:5]
            
            for game in games:
                trends.append(game.text)
            
            print(f"📈 Current Trends Found: {', '.join(trends)}")
            return trends
        except Exception as e:
            print(f"⚠️ Error during research: {e}")
            return ["Battle Royale", "Survival", "Open World"] # بيانات احتياطية

    def analyze_competitor(self, game_name):
        """تحليل منافس معين (مثل PUBG أو COD) عبر Google"""
        # محاكاة للتحليل (سيتم تطويرها لربطها بـ API بحث مجاني)
        analysis = f"Analyzing {game_name}: High engagement in multiplayer, requires optimization for mobile."
        return analysis

