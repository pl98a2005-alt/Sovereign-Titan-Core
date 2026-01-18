# main.py - V1.6 EMERGENCY SHIELD
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import os

# إعداد الشاشة سوداء ملكية
Window.clearcolor = get_color_from_hex('#000000')

class SovereignEngine(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20)
        
        # عنوان ترحيبي ثابت لا يسبب كراش
        self.add_widget(Label(
            text='SOVEREIGN ARCHITECT\n[ SYSTEM ONLINE ]',
            font_size='25sp',
            color=get_color_from_hex('#D4AF37'),
            halign='center'
        ))

        # محاولة فحص المكونات بحذر شديد
        self.error_log = ""
        try:
            import requests
            import PIL
            import sqlite3
            self.add_widget(Label(text="Core Modules: Verified ✅", color=(0, 1, 0, 1)))
        except Exception as e:
            self.error_log = str(e)
            self.add_widget(Label(text=f"Module Missing: {self.error_log[:30]}", color=(1, 0, 0, 1)))

        self.add_widget(Label(
            text='Ready for Engineering Command...',
            font_size='14sp',
            color=(0.5, 0.5, 0.5, 1)
        ))

class SovereignApp(App):
    def build(self):
        return SovereignEngine()

if __name__ == '__main__':
    try:
        SovereignApp().run()
    except Exception as e:
        # إذا حدث كراش حتى في التشغيل، سيحاول النظام كتابة السبب
        with open("crash_log.txt", "w") as f:
            f.write(str(e))
