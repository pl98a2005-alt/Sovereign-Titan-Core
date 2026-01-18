# main.py - SOVEREIGN ARCHITECT (V1.5 - VISION & STABLE)
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

# محاولة استدعاء المحرك
try:
    from ai_strategist import factory_pipeline
except Exception:
    factory_pipeline = None

class SovereignEngine(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=15, spacing=15)
        Window.clearcolor = get_color_from_hex('#000000')
        
        # الخط (تأكد من وجود font.ttf في المستودع)
        self.FONT = 'font.ttf' if os.path.exists('font.ttf') else None

        # 1. شريط اللغة
        self.top_bar = BoxLayout(size_hint_y=0.1)
        self.lang = Spinner(
            text='Language / اللغة',
            values=('English', 'العربية'),
            background_color=get_color_from_hex('#D4AF37'),
            color=(0,0,0,1), font_name=self.FONT
        )
        self.lang.bind(text=self.switch_language)
        self.top_bar.add_widget(self.lang)
        self.add_widget(self.top_bar)

        # 2. العنوان
        self.title = Label(text='SOVEREIGN ARCHITECT', font_size='26sp', color=get_color_from_hex('#D4AF37'), font_name=self.FONT)
        self.add_widget(self.title)

        # 3. مدخلات النص
        self.desc_input = TextInput(hint_text='Describe or Upload Image...', background_color=get_color_from_hex('#1A1A1A'), foreground_color=(1,1,1,1), font_name=self.FONT, size_hint_y=0.3)
        self.add_widget(self.desc_input)

        # 4. الحالة
        self.status = Label(text='AI System: Online', color=get_color_from_hex('#00FFFF'), font_name=self.FONT)
        self.add_widget(self.status)

        # 5. أزرار التحكم
        btn_layout = BoxLayout(orientation='vertical', size_hint_y=0.4, spacing=10)
        
        self.build_btn = Button(text='START ENGINEERING', background_color=get_color_from_hex('#D4AF37'), color=(0,0,0,1), font_name=self.FONT)
        self.build_btn.bind(on_press=self.run_engine)
        
        # الزر الجديد لرفع الصور
        self.vision_btn = Button(text='UPLOAD VISION (IMAGE)', background_color=get_color_from_hex('#008080'), color=(1,1,1,1), font_name=self.FONT)
        self.vision_btn.bind(on_press=self.open_file_manager)

        btn_layout.add_widget(self.build_btn)
        btn_layout.add_widget(self.vision_btn)
        self.add_widget(btn_layout)

    def switch_language(self, spinner, text):
        if text == 'العربية':
            self.title.text = 'المعماري السيادي'
            self.build_btn.text = 'بدء الهندسة'
            self.vision_btn.text = 'رفع رؤية (صورة)'
            self.status.text = 'نظام الذكاء: متصل'
        else:
            self.title.text = 'SOVEREIGN ARCHITECT'
            self.build_btn.text = 'START ENGINEERING'
            self.vision_btn.text = 'UPLOAD VISION (IMAGE)'
            self.status.text = 'AI System: Online'

    def open_file_manager(self, instance):
        # هذا الزر سيفتح مستكشف الصور (يحتاج صلاحيات أندرويد)
        self.status.text = "Opening Vision Vault..."
        # هنا يتم استدعاء ميزة اختيار الملفات

    def run_engine(self, instance):
        if factory_pipeline:
            self.status.text = "Sovereign AI is analyzing..."
            res = factory_pipeline(description=self.desc_input.text)
            self.status.text = res

class SovereignApp(App):
    def build(self): return SovereignEngine()

if __name__ == '__main__': SovereignApp().run()
