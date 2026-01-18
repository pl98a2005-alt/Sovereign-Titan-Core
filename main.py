# main.py - SOVEREIGN ARCHITECT (V1.2 - HYBRID STABLE ENGINE)
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

# محاولة استدعاء المحرك بحذر لتجنب الكراش عند بدء التشغيل
try:
    from ai_strategist import factory_pipeline
except ImportError:
    factory_pipeline = lambda x: "Error: AI Module Missing"

# إعداد الخط العربي (تأكد من وجود ملف font.ttf في المستودع)
FONT_PATH = 'font.ttf' if os.path.exists('font.ttf') else None

Window.clearcolor = get_color_from_hex('#000000')

class SovereignEngine(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10)
        
        try:
            # 1. القائمة العلوية لاختيار اللغة
            self.top_bar = BoxLayout(size_hint_y=0.1)
            self.lang_spinner = Spinner(
                text='Language / اللغة',
                values=('English', 'العربية'),
                background_color=get_color_from_hex('#D4AF37'),
                color=(0,0,0,1),
                font_name=FONT_PATH
            )
            self.lang_spinner.bind(text=self.switch_language)
            self.top_bar.add_widget(self.lang_spinner)
            self.add_widget(self.top_bar)

            # 2. النصوص والواجهة
            self.title_label = Label(
                text='SOVEREIGN ARCHITECT',
                font_size='28sp', color=get_color_from_hex('#D4AF37'),
                font_name=FONT_PATH
            )
            self.add_widget(self.title_label)

            self.description = TextInput(
                hint_text='Describe your game / صف لعبتك...', 
                background_color=get_color_from_hex('#1A1A1A'),
                foreground_color=get_color_from_hex('#FFFFFF'),
                multiline=True, size_hint_y=0.4, font_name=FONT_PATH
            )
            self.add_widget(self.description)

            self.ai_status = Label(
                text='Status: Ready', color=get_color_from_hex('#00FFFF'), font_name=FONT_PATH
            )
            self.add_widget(self.ai_status)

            # 3. أزرار التحكم (الهندسة والتنظيف)
            self.btns_layout = BoxLayout(orientation='horizontal', size_hint_y=0.15, spacing=10)
            self.build_btn = Button(text='ENGINEERING', background_color=get_color_from_hex('#D4AF37'), color=(0,0,0,1))
            self.clean_btn = Button(text='CLEAN UP', background_color=get_color_from_hex('#444444'))
            
            self.build_btn.bind(on_press=self.run_factory)
            self.clean_btn.bind(on_press=self.perform_cleanup)
            
            self.btns_layout.add_widget(self.build_btn)
            self.btns_layout.add_widget(self.clean_btn)
            self.add_widget(self.btns_layout)

        except Exception as e:
            self.add_widget(Label(text=f"UI Error: {str(e)}", font_name=FONT_PATH))

    def switch_language(self, spinner, text):
        if text == 'العربية':
            self.title_label.text = 'المعماري السيادي'
            self.description.hint_text = 'صف عظمتك البرمجية هنا...'
            self.ai_status.text = 'الحالة: جاهز للعمل'
            self.build_btn.text = 'بدء الهندسة'
            self.clean_btn.text = 'تنظيف'
        else:
            self.title_label.text = 'SOVEREIGN ARCHITECT'
            self.description.hint_text = 'Describe your game...'
            self.ai_status.text = 'Status: Ready'
            self.build_btn.text = 'ENGINEERING'
            self.clean_btn.text = 'CLEAN UP'

    def run_factory(self, instance):
        if self.description.text:
            self.ai_status.text = "Generating... / جاري التوليد..."
            result = factory_pipeline(self.description.text)
            self.ai_status.text = result

    def perform_cleanup(self, instance):
        # [2026-01-13] حذف الزوائد مع استثناء الأكواد والخبرات
        self.ai_status.text = "Cleaning up extras... / جاري تنظيف الزوائد..."

class SovereignApp(App):
    def build(self):
        return SovereignEngine()

    def on_start(self):
        # طلب الصلاحيات فوراً لتجنب الكراش عند محاولة الكتابة في الذاكرة
        try:
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        except Exception:
            pass

if __name__ == '__main__':
    SovereignApp().run()
