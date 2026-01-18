# main.py - V2.2 ARABIC & CRASH SHIELD
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import os

# [2026-01-13] مكتبات معالجة العربية لضمان عدم ظهور مربعات
try:
    from arabic_reshaper import reshape
    from bidi.algorithm import get_display
except:
    reshape = lambda x: x
    get_display = lambda x: x

Window.clearcolor = get_color_from_hex('#000000')

class SovereignEngine(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=15, spacing=10)
        # استخدام ملف font.ttf الموجود في مستودعك
        self.FONT = 'font.ttf' if os.path.exists('font.ttf') else None

        self.add_widget(Label(
            text='SOVEREIGN TITAN FACTORY',
            font_size='26sp', color=get_color_from_hex('#D4AF37'),
            font_name=self.FONT
        ))

        self.desc_input = TextInput(
            hint_text='Command your Engineer...',
            size_hint_y=0.25, background_color=(0.1, 0.1, 0.1, 1), 
            foreground_color=(1, 1, 1, 1), font_name=self.FONT
        )
        self.add_widget(self.desc_input)

        self.status = Label(text='Factory Status: Online ✅', color=(0, 1, 0.5, 1), font_name=self.FONT)
        self.add_widget(self.status)

        self.build_btn = Button(
            text='START AUTONOMOUS ENGINEERING',
            background_color=get_color_from_hex('#D4AF37'),
            color=(0,0,0,1), font_name=self.FONT
        )
        self.build_btn.bind(on_press=self.run_ai)
        self.add_widget(self.build_btn)

    def run_ai(self, instance):
        try:
            from ai_strategist import factory_pipeline
            res = factory_pipeline(description=self.desc_input.text)
            # معالجة النص العربي قبل العرض
            self.status.text = get_display(reshape(res))
        except Exception as e:
            self.status.text = f"Error: {str(e)[:30]}"

class SovereignApp(App):
    def build(self):
        return SovereignEngine()

    def on_start(self):
        # طلب صلاحيات الإنترنت والذاكرة [2026-01-18]
        try:
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.INTERNET, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
        except: pass

if __name__ == '__main__':
    SovereignApp().run()
