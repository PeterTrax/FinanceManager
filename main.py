from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from sourcecode import sourcecode
from kivymd.uix.boxlayout import MDBoxLayout

Window.size = (400, 700)


class FinanceManagementApp(MDApp):
    TransanctionSearchData = { 
        'Search by date': 'calendar',
        'Search by category': 'clipboard-list',
        'Search by amount': 'currency-eur'    
    }

    def build(self):
        screen = Builder.load_string(sourcecode)
        return screen


FinanceManagementApp().run()
