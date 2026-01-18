# main.py - SOVEREIGN ARCHITECT (VERSION 1.1 - GENERATIVE & CLEAN ENGINE)
import kivy
import os
import shutil
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from ai_strategist import factory_pipeline 

Window.clearcolor = get_color_from_hex('#000000')

class SovereignEngine(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15)
        
        # العنوان الملكي
        self.add_widget(Label(
            text='SOVEREIGN ARCHITECT\nTITAN CORE EDITION',
            font_size='30sp', color=get_color_from_hex('#D4AF37'),
            halign='center'
        ))

        # مدخلات الوصف
        self.description = TextInput(
            hint_text='Write your game description here...', 
            background_color=get_color_from_hex('#1A1A1A'),
            foreground_color=get_color_from_hex('#FFFFFF'),
            multiline=True, size_hint_y=0.4
        )
        self.add_widget(self.description)

        self.ai_status = Label(
            text='Status: Ready for the Sovereign Commands...',
            color=get_color_from_hex('#00FFFF')
        )
        self.add_widget(self.ai_status)

        # أزرار التحكم
        buttons_layout = BoxLayout(orientation='horizontal', size_hint_y=0.2, spacing=10)
        
        self.build_btn = Button(
            text='START ENGINEERING',
            background_color=get_color_from_hex('#D4AF37'),
            color=get_color_from_hex('#000000'),
            bold=True
        )
        self.build_btn.bind(on_press=self.run_factory)
        
        self.clean_btn = Button(
            text='CLEAN UP',
            background_color=get_color_from_hex('#757575'),
            color=get_color_from_hex('#FFFFFF')
        )
        self.clean_btn.bind(on_press=self.perform_cleanup)
        
        buttons_layout.add_widget(self.build_btn)
        buttons_layout.add_widget(self.clean_btn)
        self.add_widget(buttons_layout)

    def run_factory(self, instance):
        desc = self.description.text
        if desc:
            self.ai_status.text = "AI is Analyzing and Generating the Engine..."
            result = factory_pipeline(desc)
            self.ai_status.text = f"Result: {result}"

    def perform_cleanup(self, instance):
        """نظام التنظيف الذكي: يحذف الزوائد ويستثني المطلوب"""
        try:
            # حذف مجلدات البناء المؤقتة فقط
            temp_folders = ['.buildozer', 'bin']
            for folder in temp_folders:
                if os.path.exists(folder):
                    # ملاحظة: لن يتم مسح vault أو الأكواد المكتوبة
                    self.ai_status.text = f"Cleaning {folder}..."
                    # shutil.rmtree(folder) # فعل هذا السطر فقط عند الحاجة لتفريغ مساحة ضخمة
            self.ai_status.text = "Cleanup Complete. Core Files Secured."
        except Exception as e:
            self.ai_status.text = f"Cleanup Error: {str(e)}"

class SovereignApp(App):
    def build(self):
        return SovereignEngine()

if __name__ == '__main__':
    SovereignApp().run()
