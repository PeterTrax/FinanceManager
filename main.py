from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from sourcecode import sourcecode
from kivymd.uix.boxlayout import MDBoxLayout

Window.size = (400, 700)


class FinanceManagementApp(MDApp):
    def build(self):
        screen = Builder.load_string(sourcecode)
        return screen


FinanceManagementApp().run()
