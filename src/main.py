from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, RoundedRectangle
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from threading import Thread
import random, time, os

from ai_strategist import factory_pipeline, GraphicsScraper, auto_optimize_database

try:
    from arabic_reshaper import reshape
    from bidi.algorithm import get_display
    def ar(t): return get_display(reshape(str(t)))
except:
    def ar(t): return str(t)

class SovereignEngine(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = get_color_from_hex('#050505')
        
        self.status = Label(text=ar("العقل: متصل | النظام: مستقر"), size_hint=(1, 0.1), pos_hint={'top': 1}, color=(1, 0.84, 0, 1))
        self.add_widget(self.status)

        self.input = TextInput(hint_text=ar("صف اللعبة أو الميزة الهندسيّة..."), size_hint=(0.9, 0.1), pos_hint={'center_x': 0.5, 'top': 0.85}, background_color=(0.1, 0.1, 0.1, 1), foreground_color=(1, 1, 1, 1))
        self.add_widget(self.input)

        self.btn_run = Button(text=ar("إرسال للأتمتة"), size_hint=(0.4, 0.1), pos_hint={'x': 0.05, 'top': 0.7}, background_color=get_color_from_hex('#D4AF37'))
        self.btn_run.bind(on_release=self.process_ai)
        self.add_widget(self.btn_run)

        self.btn_scrape = Button(text=ar("جمع خبرات"), size_hint=(0.4, 0.1), pos_hint={'right': 0.95, 'top': 0.7}, background_color=get_color_from_hex('#D4AF37'))
        self.btn_scrape.bind(on_release=self.process_scrape)
        self.add_widget(self.btn_scrape)

        self.btn_clean = Button(text=ar("Clean-up"), size_hint=(0.3, 0.08), pos_hint={'center_x': 0.5, 'top': 0.58}, background_color=get_color_from_hex('#A52A2A'))
        self.btn_clean.bind(on_release=self.process_clean)
        self.add_widget(self.btn_clean)

        self.log = Label(text=ar("بانتظار الأوامر..."), size_hint=(0.9, 0.3), pos_hint={'center_x': 0.5, 'y': 0.1}, color=(0, 1, 0, 1), font_size='14sp')
        self.add_widget(self.log)

    def process_ai(self, instance):
        Thread(target=self.run_ai).start()
    def run_ai(self):
        res = factory_pipeline(self.input.text)
        Clock.schedule_once(lambda dt: setattr(self.log, 'text', ar(res)))

    def process_scrape(self, instance):
        Thread(target=self.run_scrape).start()
    def run_scrape(self):
        res = GraphicsScraper.scrape_graphics_logic()
        Clock.schedule_once(lambda dt: setattr(self.log, 'text', ar(res)))

    def process_clean(self, instance):
        res = auto_optimize_database()
        self.log.text = ar(res)

class SovereignApp(App):
    def build(self): return SovereignEngine()

if __name__ == '__main__': SovereignApp().run()
