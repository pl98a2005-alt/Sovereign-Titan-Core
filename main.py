# main.py - SOVEREIGN ARCHITECT (V1.3 - EMERGENCY STABLE)
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import os

# إعدادات الشاشة
Window.clearcolor = get_color_from_hex('#000000')

class SovereignEngine(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=20)
        
        # رسالة ترحيب بسيطة للتأكد من أن الواجهة تعمل
        self.add_widget(Label(
            text='SOVEREIGN ARCHITECT\nTITAN CORE IS ALIVE',
            font_size='24sp', 
            color=get_color_from_hex('#D4AF37'),
            halign='center'
        ))

        # محاولة فحص المحرك داخلياً
        try:
            from ai_strategist import AIStrategist
            self.status = Label(text='AI System: Connected', color=(0,1,1,1))
        except Exception as e:
            self.status = Label(text=f'AI Error: {str(e)[:30]}', color=(1,0,0,1))
        
        self.add_widget(self.status)

        # زر اختبار بسيط
        self.btn = Button(
            text='ENTER THE VAULT',
            size_hint_y=0.2,
            background_color=get_color_from_hex('#D4AF37'),
            color=(0,0,0,1)
        )
        self.add_widget(self.btn)

class SovereignApp(App):
    def build(self):
        return SovereignEngine()

    def on_start(self):
        # طلب الصلاحيات بطريقة آمنة جداً
        try:
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
        except:
            pass

if __name__ == '__main__':
    SovereignApp().run()
