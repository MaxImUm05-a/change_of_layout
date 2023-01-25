from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.behaviors import MagicBehavior
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
import main

class MyButton(MDRectangleFlatButton, MagicBehavior):
    def on_release(self):
        super().on_release()
        main.add()

class ChangeLayout(MDApp):
    def build(self):
        bl = MDBoxLayout(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            adaptive_size = True,
            size_hint = (0.5, 0.5),
            orientation = 'vertical'
        )
        btn = MyButton(text = 'start', pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        lab1 = MDLabel(text = 'Програма, щоб переводити написаний текст з англійської розкладки на українську',
                      bold = True, font_size = '100dp')
        lab2 = MDLabel(text = 'Автор:\nМаксим, той що з Вараша\nОсь його нік в Github:\nMaxImUm05-a', font_size = '50dp')
        bl.add_widget(lab1)
        bl.add_widget(btn)
        bl.add_widget(lab2)
        return bl

if __name__ == '__main__':
    ChangeLayout().run()