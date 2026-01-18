# main.py - SOVEREIGN TITAN ULTIMATE V3.0
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import os

# نظام معالجة العربية لضمان عدم ظهور مربعات [2026-01-13]
try:
    from arabic_reshaper import reshape
    from bidi.algorithm import get_display
    def ar(text): return get_display(reshape(text))
except:
    def ar(text): return text

Window.clearcolor = get_color_from_hex('#050505')

class SovereignEngine(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15)
        # التأكد من وجود ملف الخط الذي رفعته باسم font.ttf
        self.FONT = 'font.ttf' if os.path.exists('font.ttf') else None

        # شعار المصنع
        self.add_widget(Label(
            text="TITAN CORE ENGINE",
            font_size='30sp', bold=True, color=get_color_from_hex('#D4AF37'),
            size_hint_y=0.15
        ))

        # صندوق المدخلات المطور
        self.desc_input = TextInput(
            hint_text=ar("اكتب وصف اللعبة أو المشروع هنا..."),
            size_hint_y=0.4, font_name=self.FONT,
            background_color=(0.12, 0.12, 0.12, 1),
            foreground_color=(1, 1, 1, 1),
            font_size='20sp', padding=[15, 15],
            cursor_color=get_color_from_hex('#D4AF37')
        )
        self.add_widget(self.desc_input)

        # حالة النظام
        self.status = Label(
            text=ar("بانتظار الأوامر الملكية... ✅"),
            color=(0.6, 0.6, 0.6, 1), font_name=self.FONT,
            size_hint_y=0.1, font_size='16sp'
        )
        self.add_widget(self.status)

        # زر الهندسة
        self.build_btn = Button(
            text=ar("بدء الهندسة الذاتية"),
            background_normal='', background_color=get_color_from_hex('#D4AF37'),
            color=(0,0,0,1), font_name=self.FONT,
            font_size='24sp', bold=True, size_hint_y=0.15
        )
        self.build_btn.bind(on_press=self.run_ai)
        self.add_widget(self.build_btn)

    def run_ai(self, instance):
        if not self.desc_input.text.strip():
            self.status.text = ar("يرجى إدخال وصف أولاً!")
            return
        try:
            from ai_strategist import factory_pipeline
            self.status.text = ar("تيتان يحلل ويستنتج الآن...")
            res = factory_pipeline(description=self.desc_input.text)
            self.status.text = ar(res)
        except Exception as e:
            self.status.text = ar(f"خطأ في الربط: {str(e)[:30]}")

class SovereignApp(App):
    def build(self): return SovereignEngine()
    def on_start(self):
        try:
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.INTERNET, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
        except: pass

if __name__ == '__main__': SovereignApp().run()
