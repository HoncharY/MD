import kivy
kivy.require("1.11.1")
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.config import Config
Config.set('graphics', 'resizable', True)
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle

class Lab3App(App):

    def build(self):
            start=Widget()

            # button1


            btn1 = Button()
            lbl1 = Label(text="Star Wars:Episode IV - A \nNew Hope \n\n1977 \n\n\nmovie")
            start.add_widget(lbl1)
            start.add_widget(btn1)
            lbl1.center_x = 240
            lbl1.center_y = 770
            btn1.center_x = 50
            btn1.center_y = 690
            btn1.background_normal = "Poster_01.jpg"
            btn1.size = 150,200

            # button2

            btn2 = Button()
            lbl2 = Label(text="Star Wars:Episode V - The \nEmpire Strikes Back \n\n1980 \n\n\nmovie")
            start.add_widget(lbl2)
            start.add_widget(btn2)
            lbl2.center_x = 585
            lbl2.center_y = 770
            btn2.center_x = 390
            btn2.center_y = 685
            btn2.background_normal = "Poster_02.jpg"
            btn2.size = 150, 200

            # button3

            btn3 = Button()
            lbl3 = Label(text="Star Wars:Episode VI - Return of \nthe Jedi \n\n1983 \n\n\nmovie")
            start.add_widget(lbl3)
            start.add_widget(btn3)
            lbl3.center_x = 955
            lbl3.center_y = 770
            btn3.center_x = 740
            btn3.center_y = 690
            btn3.background_normal = "Poster_03.jpg"
            btn3.size = 150, 200

            # button4

            btn4 = Button()
            lbl4 = Label(text="Star Wars:Episode I - The \nPhantom Menace \n\n1999 \n\n\nmovie")
            start.add_widget(lbl4)
            start.add_widget(btn4)
            lbl4.center_x = 1350
            lbl4.center_y = 770
            btn4.center_x = 1125
            btn4.center_y = 660
            btn4.background_normal = "Poster_05.jpg"
            btn4.size = 190, 240




            return start





root = Lab3App()

root.run()