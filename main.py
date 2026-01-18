from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
import os

class SovereignEngine(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=15, spacing=10)
        Window.clearcolor = get_color_from_hex('#000000')
        self.FONT = 'font.ttf' if os.path.exists('font.ttf') else None

        # واجهة بسيطة في البداية لمنع الكراش
        self.title = Label(text='SOVEREIGN ARCHITECT', font_size='26sp', color=get_color_from_hex('#D4AF37'), font_name=self.FONT)
        self.add_widget(self.title)

        self.desc_input = TextInput(hint_text='Describe your game...', size_hint_y=0.3, font_name=self.FONT)
        self.add_widget(self.desc_input)

        self.status = Label(text='AI System: Ready', color=get_color_from_hex('#00FFFF'), font_name=self.FONT)
        self.add_widget(self.status)

        # الأزرار
        self.build_btn = Button(text='START ENGINEERING', background_color=get_color_from_hex('#D4AF37'), font_name=self.FONT)
        self.build_btn.bind(on_press=self.run_ai)
        self.add_widget(self.build_btn)

        self.clean_btn = Button(text='CLEAN UP', background_color=get_color_from_hex('#444444'), font_name=self.FONT)
        self.clean_btn.bind(on_press=self.do_clean)
        self.add_widget(self.clean_btn)

    def run_ai(self, instance):
        from ai_strategist import factory_pipeline
        self.status.text = "Sovereign AI is analyzing..."
        res = factory_pipeline(description=self.desc_input.text)
        self.status.text = res

    def do_clean(self, instance):
        self.status.text = "Cleaning... Vault is safe."

class SovereignApp(App):
    def build(self): return SovereignEngine()

if __name__ == '__main__': SovereignApp().run()
