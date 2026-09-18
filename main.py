import sqlite3
from kivy.lang import Builder
from kivymd.app import MDApp

class AlDimashqiAccApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string('''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "الدمشقي للمحاسبة"
        MDBoxLayout:
            orientation: 'vertical'
            padding: "20dp"
            MDLabel:
                text: "تطبيق الدمشقي للمحاسبة"
                halign: "center"
''')

if __name__ == '__main__':
    AlDimashqiAccApp().run()
