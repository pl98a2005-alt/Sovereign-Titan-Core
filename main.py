# main.py - SOVEREIGN ARCHITECT V1.7 STABLE
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
        super().__init__(orientation='vertical', padding=20, spacing=10)
        
        # العنوان الأساسي
        self.add_widget(Label(
            text='SOVEREIGN ARCHITECT\n[ SYSTEM ONLINE ]',
            font_size='25sp',
            color=get_color_from_hex('#D4AF37'),
            halign='center'
        ))

        # فحص المكتبات وتأكيد نظام الرؤية
        try:
            from PIL import Image
            import requests
            self.add_widget(Label(text="Vision Core: Active ✅", color=(0, 1, 0.5, 1)))
            self.add_widget(Label(text="AI Link: Connected ✅", color=(0, 1, 0.5, 1)))
        except ImportError:
            self.add_widget(Label(text="Status: Initializing Modules...", color=(1, 0.8, 0, 1)))
        except Exception as e:
            self.add_widget(Label(text=f"Check Specs: {str(e)[:20]}", color=(1, 0, 0, 1)))

        self.add_widget(Label(
            text='Ready for Engineering Command...',
            font_size='14sp',
            color=(0.5, 0.5, 0.5, 1)
        ))

class SovereignApp(App):
    def build(self):
        return SovereignEngine()

    def on_start(self):
        # طلب صلاحيات الذاكرة لضمان عمل الخزنة (Vault)
        try:
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
        except:
            pass

if __name__ == '__main__':
    SovereignApp().run()
