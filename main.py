from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
import os

class SovereignEngine(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=15, spacing=15)
        # تشغيل الواجهة بأبسط صورة لمنع الكراش
        self.title = Label(text='TITAN CORE LOADING...', font_size='24sp', color=(0.83, 0.69, 0.22, 1))
        self.add_widget(self.title)
        
        # تأجيل تحميل المكونات الثقيلة لثانية واحدة
        Clock.schedule_once(self.load_full_system, 1)

    def load_full_system(self, dt):
        try:
            # الآن نحمل الخط والذكاء بعد أن استقر التطبيق
            FONT = 'font.ttf' if os.path.exists('font.ttf') else None
            self.title.text = 'SOVEREIGN ARCHITECT'
            if FONT: self.title.font_name = FONT
            
            self.desc = TextInput(hint_text='Describe...', size_hint_y=0.4, font_name=FONT)
            self.add_widget(self.desc)
            
            self.btn = Button(text='START ENGINEERING', size_hint_y=0.2, font_name=FONT)
            self.btn.bind(on_press=self.run_ai)
            self.add_widget(self.btn)
        except Exception as e:
            self.add_widget(Label(text=f"Error: {str(e)}"))

    def run_ai(self, instance):
        from ai_strategist import factory_pipeline
        res = factory_pipeline(self.desc.text)
        self.title.text = "Success!"

class SovereignApp(App):
    def build(self): return SovereignEngine()

if __name__ == '__main__': SovereignApp().run()
