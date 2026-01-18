# main.py - SOVEREIGN ARCHITECT (DUAL LANGUAGE SYSTEM)
import kivy
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from ai_strategist import factory_pipeline 

# إعداد الخط العربي (يجب رفعه للمستودع باسم font.ttf)
FONT_PATH = 'font.ttf' if os.path.exists('font.ttf') else None

class SovereignEngine(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10)
        
        # 1. القائمة العلوية لاختيار اللغة
        self.top_bar = BoxLayout(size_hint_y=0.1)
        self.lang_spinner = Spinner(
            text='Language / اللغة',
            values=('English', 'العربية'),
            background_color=get_color_from_hex('#D4AF37'),
            color=(0,0,0,1)
        )
        self.lang_spinner.bind(text=self.switch_language)
        self.top_bar.add_widget(self.lang_spinner)
        self.add_widget(self.top_bar)

        # 2. النصوص القابلة للتغيير
        self.title_label = Label(
            text='SOVEREIGN ARCHITECT',
            font_size='28sp', color=get_color_from_hex('#D4AF37'),
            font_name=FONT_PATH
        )
        self.add_widget(self.title_label)

        self.description = TextInput(
            hint_text='Describe your game...', 
            background_color=get_color_from_hex('#1A1A1A'),
            foreground_color=get_color_from_hex('#FFFFFF'),
            multiline=True, size_hint_y=0.4, font_name=FONT_PATH
        )
        self.add_widget(self.description)

        self.ai_status = Label(
            text='Status: Ready', color=get_color_from_hex('#00FFFF'), font_name=FONT_PATH
        )
        self.add_widget(self.ai_status)

        # 3. أزرار التحكم
        self.btns_layout = BoxLayout(orientation='horizontal', size_hint_y=0.15, spacing=10)
        self.build_btn = Button(text='ENGINEERING', background_color=get_color_from_hex('#D4AF37'), color=(0,0,0,1))
        self.clean_btn = Button(text='CLEAN UP', background_color=get_color_from_hex('#444444'))
        
        self.build_btn.bind(on_press=self.run_factory)
        self.clean_btn.bind(on_press=self.perform_cleanup)
        
        self.btns_layout.add_widget(self.build_btn)
        self.btns_layout.add_widget(self.clean_btn)
        self.add_widget(self.btns_layout)

    def switch_language(self, spinner, text):
        """تغيير لغة الواجهة فوراً"""
        if text == 'العربية':
            self.title_label.text = 'المعماري السيادي'
            self.description.hint_text = 'صف لعبتك هنا...'
            self.ai_status.text = 'الحالة: جاهز للأوامر'
            self.build_btn.text = 'بدء الهندسة'
            self.clean_btn.text = 'تنظيف'
        else:
            self.title_label.text = 'SOVEREIGN ARCHITECT'
            self.description.hint_text = 'Describe your game...'
            self.ai_status.text = 'Status: Ready'
            self.build_btn.text = 'ENGINEERING'
            self.clean_btn.text = 'CLEAN UP'

    def run_factory(self, instance):
        # الـ AI يعالج اللغتين تلقائياً كما ذكرت يا شريكي
        result = factory_pipeline(self.description.text)
        self.ai_status.text = result

    def perform_cleanup(self, instance):
        # استثناء الملفات المطلوبة مثل الخبرات المكتسبة
        self.ai_status.text = "Cleaning... / جاري التنظيف..."
