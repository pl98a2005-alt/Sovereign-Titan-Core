# main.py - V2.0 CRASH SHIELD & TITAN LINK
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
import os

Window.clearcolor = get_color_from_hex('#000000')

class SovereignEngine(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=15, spacing=10)
        
        # العنوان
        self.add_widget(Label(
            text='SOVEREIGN TITAN FACTORY',
            font_size='26sp', color=get_color_from_hex('#D4AF37')
        ))

        # صندوق المدخلات
        self.desc_input = TextInput(
            hint_text='Command your Engineer...',
            size_hint_y=0.25, background_color=(0.1, 0.1, 0.1, 1), 
            foreground_color=(1, 1, 1, 1)
        )
        self.add_widget(self.desc_input)

        self.status = Label(text='Factory Status: Online ✅', color=(0, 1, 0.5, 1))
        self.add_widget(self.status)

        # زر الهندسة (مربوط بالعقل المطور)
        self.build_btn = Button(
            text='START AUTONOMOUS ENGINEERING',
            background_color=get_color_from_hex('#D4AF37'),
            color=(0,0,0,1)
        )
        self.build_btn.bind(on_press=self.run_ai)
        self.add_widget(self.build_btn)

    def run_ai(self, instance):
        try:
            # التأكد من استدعاء الكلاس الجديد SovereignTitanAI [2026-01-18]
            from ai_strategist import factory_pipeline
            self.status.text = "AI Searching & Learning..."
            res = factory_pipeline(description=self.desc_input.text)
            self.status.text = res
        except Exception as e:
            # منع الكراش وعرض الخطأ بدلاً من الخروج
            self.status.text = f"Internal Error: {str(e)[:30]}"

class SovereignApp(App):
    def build(self):
        return SovereignEngine()

    def on_start(self):
        # طلب الصلاحيات فوراً لمنع الكراش عند محاولة القراءة أو الاتصال [2026-01-18]
        try:
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.INTERNET, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
        except:
            pass

if __name__ == '__main__':
    SovereignApp().run()
