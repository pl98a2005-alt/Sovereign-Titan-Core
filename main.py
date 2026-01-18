# main.py - SOVEREIGN ARCHITECT V1.8 FINAL
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import os

Window.clearcolor = get_color_from_hex('#000000')

class SovereignEngine(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=15, spacing=10)
        self.FONT = 'font.ttf' if os.path.exists('font.ttf') else None

        # العنوان
        self.add_widget(Label(
            text='SOVEREIGN ARCHITECT',
            font_size='26sp', color=get_color_from_hex('#D4AF37'),
            font_name=self.FONT
        ))

        # مدخلات الهندسة
        self.desc_input = TextInput(
            hint_text='Describe your game concept...',
            size_hint_y=0.3, font_name=self.FONT,
            background_color=(0.1, 0.1, 0.1, 1), foreground_color=(1, 1, 1, 1)
        )
        self.add_widget(self.desc_input)

        # الحالة
        self.status = Label(text='System Ready ✅', color=(0, 1, 0.5, 1), font_name=self.FONT)
        self.add_widget(self.status)

        # أزرار التحكم
        self.build_btn = Button(
            text='START ENGINEERING',
            background_color=get_color_from_hex('#D4AF37'),
            color=(0,0,0,1), font_name=self.FONT
        )
        self.build_btn.bind(on_press=self.run_ai)
        self.add_widget(self.build_btn)

        self.vision_btn = Button(text='UPLOAD VISION (IMAGE)', font_name=self.FONT)
        self.add_widget(self.vision_btn)

    def run_ai(self, instance):
        try:
            from ai_strategist import factory_pipeline
            self.status.text = "AI Analyzing..."
            res = factory_pipeline(description=self.desc_input.text)
            self.status.text = res
        except Exception as e:
            self.status.text = f"Link Error: {str(e)[:20]}"

class SovereignApp(App):
    def build(self): return SovereignEngine()

if __name__ == '__main__': SovereignApp().run()
