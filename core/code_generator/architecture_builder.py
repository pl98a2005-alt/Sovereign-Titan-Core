import json, os

class ArchitectureBuilder:
    def __init__(self, concept_path):
        with open(concept_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        self.project_name = self.data.get('game_title', 'NewGame').replace(" ", "_")

    def create_game_files(self):
        os.makedirs(f"games/{self.project_name}", exist_ok=True)
        code = f"""
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel

class {self.project_name}App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        screen = MDScreen()
        screen.add_widget(MDLabel(text="Game: {self.data.get('game_title')}\\nGenre: {self.data.get('genre')}", halign="center"))
        return screen

if __name__ == "__main__":
    {self.project_name}App().run()
"""
        with open(f"games/{self.project_name}/main.py", "w", encoding='utf-8') as f:
            f.write(code)
        return f"✅ Done: games/{self.project_name}/main.py"

