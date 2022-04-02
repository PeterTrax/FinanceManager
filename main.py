from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from appcode import screens

Window.size = (400, 700)


class FinanceManagementApp(MDApp):

    def build(self):
        screen = Builder.load_string(screens)
        return screen


FinanceManagementApp().run()
