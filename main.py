# main.py - SOVEREIGN ARCHITECT (V1.4 - FULL POWER & STABLE)
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import os

# محاولة ربط العقل المدبر بحذر
try:
    from ai_strategist import factory_pipeline
except Exception:
    factory_pipeline = lambda x: "AI Connection Pending..."

# إعداد الخط - إذا لم يجد الخط سيستخدم الافتراضي لمنع الكراش
FONT_NAME = 'font.ttf' if os.path.exists('font.ttf') else None

Window.clearcolor = get_color_from_hex('#000000')

class SovereignEngine(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=15, spacing=15)
        
        # 1. شريط اللغة العلوي
        self.top_bar = BoxLayout(size_hint_y=0.1)
        self.lang_spinner = Spinner(
            text='Language / اللغة',
            values=('English', 'العربية'),
            background_color=get_color_from_hex('#D4AF37'),
            color=(0,0,0,1),
            font_name=FONT_NAME
        )
        self.lang_spinner.bind(text=self.switch_language)
        self.top_bar.add_widget(self.lang_spinner)
        self.add_widget(self.top_bar)

        # 2. العنوان
        self.title = Label(
            text='SOVEREIGN ARCHITECT',
            font_size='28sp', color=get_color_from_hex('#D4AF37'),
            font_name=FONT_NAME
        )
        self.add_widget(self.title)

        # 3. صندوق الوصف (إصلاح المربعات)
        self.desc_input = TextInput(
            hint_text='Describe your game here...',
            background_color=get_color_from_hex('#1A1A1A'),
            foreground_color=get_color_from_hex('#FFFFFF'),
            font_name=FONT_NAME,
            size_hint_y=0.4
        )
        self.add_widget(self.desc_input)

        # 4. حالة الذكاء الاصطناعي
        self.status = Label(
            text='AI System: Connected',
            color=get_color_from_hex('#00FFFF'),
            font_name=FONT_NAME
        )
        self.add_widget(self.status)

        # 5. أزرار التحكم
        btn_layout = BoxLayout(orientation='horizontal', size_hint_y=0.2, spacing=10)
        self.build_btn = Button(text='ENGINEERING', background_color=get_color_from_hex('#D4AF37'), color=(0,0,0,1), font_name=FONT_NAME)
        self.clean_btn = Button(text='CLEAN UP', background_color=get_color_from_hex('#444444'), font_name=FONT_NAME)
        
        self.build_btn.bind(on_press=self.start_build)
        self.clean_btn.bind(on_press=self.start_clean)
        
        btn_layout.add_widget(self.build_btn)
        btn_layout.add_widget(self.clean_btn)
        self.add_widget(btn_layout)

    def switch_language(self, spinner, text):
        if text == 'العربية':
            self.title.text = 'المعماري السيادي'
            self.desc_input.hint_text = 'صف لعبتك هنا...'
            self.status.text = 'نظام الذكاء: متصل'
            self.build_btn.text = 'بدء الهندسة'
            self.clean_btn.text = 'تنظيف'
        else:
            self.title.text = 'SOVEREIGN ARCHITECT'
            self.desc_input.hint_text = 'Describe your game here...'
            self.status.text = 'AI System: Connected'
            self.build_btn.text = 'ENGINEERING'
            self.clean_btn.text = 'CLEAN UP'

    def start_build(self, instance):
        if self.desc_input.text:
            self.status.text = "Generating... / جاري التوليد..."
            # استدعاء المحرك المدمج
            res = factory_pipeline(self.desc_input.text)
            self.status.text = res

    def start_clean(self, instance):
        self.status.text = "Cleaning... / جاري التنظيف..."

class SovereignApp(App):
    def build(self):
        return SovereignEngine()

    def on_start(self):
        try:
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
        except:
            pass

if __name__ == '__main__':
    SovereignApp().run()
