#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.config import Config
from kivy.lang import Builder
from kivy.core.window import Window

Config.set('graphics', 'resizable', 0)
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (720, 480)

import random

Builder.load_string('''
<Main>:
    FloatLayout:



        Image:
            source: "kino.jpg"
            allow_stretch: True
        Button:
            text:'List Movies'
            color: (30,170,60,100)
            on_press:root.manager.current='second'
            background_color: (0,0,0,0)
            size_hint: (.320,.200)
            pos: (240,270)





<Second>:
    FloatLayout:

        Button:                        #Button1
            text:''
            on_press:root.manager.current='third'
            size_hint:(.150,.300)
            pos: (1,335)
            background_normal: "Poster_01.jpg"


    FloatLayout:

        Button:                       #Button2
            text:''
            on_press:root.manager.current='fourth'
            size_hint:(.150,.300)
            pos: (1,140)
            background_normal: "Poster_02.jpg"

    FloatLayout:

        Button:                      #Button3
            text:''
            on_press:root.manager.current='fiveth'
            size_hint:(.150,.300)
            pos: (200,335)
            background_normal: "Poster_03.jpg"

    FloatLayout:

        Button:             #Button4
            text:''
            on_press:root.manager.current='sixth'
            size_hint:(.215,.355)
            pos: (185,125)
            background_normal: "Poster_05.jpg"

    FloatLayout:

        Button:             #Button5
            text:''
            on_press:root.manager.current='seventh'
            size_hint:(.190,.300)
            pos: (385,335)
            background_normal: "Poster_06.jpg"

    FloatLayout:

        Button:             #Button6
            text:''
            on_press:root.manager.current='eightth'
            size_hint:(.150,.300)
            pos: (390,140)
            background_normal: "Poster_07.jpg"

    FloatLayout:

        Button:             #Button7
            text:''
            on_press:root.manager.current='nineth'
            size_hint:(.150,.300)
            pos: (610,335)
            background_normal: "Poster_08.jpg"

    FloatLayout:

        Button:             #Button8
            text:''
            on_press:root.manager.current='tenth'
            size_hint:(.150,.300)
            pos: (610,140)
            background_normal: "Poster_10.jpg"




    FloatLayout:

        Button:                 #Button Back
            text: "back"
            on_press:root.manager.current = "first"
            size_hint:(.800,.100)
            pos: (75,20)




<Third>:
    FloatLayout:
        Image:
            source: "Poster_01.jpg"
            size: (400,400)
            pos: (-205,0)

        Button:
            text: "Back"
            on_press: root.manager.current = "second"
            size_hint:(.500,.100)
            pos: (330,10)       

        Label:
            text: "Star Wars:Episode IV - A New Hope 1977 movie"
            pos: (120, 200)

        Image:
            source: "YT.png"
            size_hint:(.500,.500)
            pos:(330,100)

<Fourth>:
    FloatLayout:
        Image:
            source: "Poster_02.jpg"
            size: (400,400)
            pos: (-205,0)

        Button:
            text: "Back"
            on_press: root.manager.current = "second"
            size_hint:(.500,.100)
            pos: (330,10)       

        Label:
            text: "Star Wars:Episode V - The Empire Strikes Back 1980 movie"
            pos: (150, 200)

        Image:
            source: "YT.png"
            size_hint:(.500,.500)
            pos:(330,100)

<Fiveth>:
    FloatLayout:
        Image:
            source: "Poster_03.jpg"
            size: (400,400)
            pos: (-205,0)

        Button:
            text: "Back"
            on_press: root.manager.current = "second"
            size_hint:(.500,.100)
            pos: (330,10)       

        Label:
            text: "Star Wars:Episode VI - Return of the Jedi 1983 movie"
            pos: (150, 200)

        Image:
            source: "YT.png"
            size_hint:(.500,.500)
            pos:(330,100)

<Sixth>:
    FloatLayout:
        Image:
            source: "Poster_05.jpg"
            size: (400,400)
            pos: (-205,0)

        Button:
            text: "Back"
            on_press: root.manager.current = "second"
            size_hint:(.500,.100)
            pos: (330,10)       

        Label:
            text: "Star Wars:Episode I - The Phantom Menace 1999 movie"
            pos: (150, 200)

        Image:
            source: "YT.png"
            size_hint:(.500,.500)
            pos:(330,100)

<Seventh>:
    FloatLayout:
        Image:
            source: "Poster_06.jpg"
            size: (400,400)
            pos: (-205,0)

        Button:
            text: "Back"
            on_press: root.manager.current = "second"
            size_hint:(.500,.100)
            pos: (330,10)       

        Label:
            text: "Star Wars: Episode III - Revenge of the Sith 2005 movie"
            pos: (150, 200)

        Image:
            source: "YT.png"
            size_hint:(.500,.500)
            pos:(330,100)

<Eightth>:
    FloatLayout:
        Image:
            source: "Poster_07.jpg"
            size: (400,400)
            pos: (-205,0)

        Button:
            text: "Back"
            on_press: root.manager.current = "second"
            size_hint:(.500,.100)
            pos: (330,10)       

        Label:
            text: "Star Wars: Episode II - Attack of the clones 2002 movie"
            pos: (150, 200)

        Image:
            source: "YT.png"
            size_hint:(.500,.500)
            pos:(330,100)

<Nineth>:
    FloatLayout:
        Image:
            source: "Poster_08.jpg"
            size: (400,400)
            pos: (-205,0)

        Button:
            text: "Back"
            on_press: root.manager.current = "second"
            size_hint:(.500,.100)
            pos: (330,10)       

        Label:
            text: "Star Trek 2009 movie"
            pos: (150, 200)

        Image:
            source: "YT.png"
            size_hint:(.500,.500)
            pos:(330,100)

<Tenth>:
    FloatLayout:
        Image:
            source: "Poster_10.jpg"
            size: (400,400)
            pos: (-205,0)

        Button:
            text: "Back"
            on_press: root.manager.current = "second"
            size_hint:(.500,.100)
            pos: (330,10)       

        Label:
            text: "Rogue One: A Star Wars Story"
            pos: (150, 200)

        Image:
            source: "YT.png"
            size_hint:(.500,.500)
            pos:(330,100)






''')


class Main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.flag = True


class Second(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Third(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Fourth(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Fiveth(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Sixth(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Seventh(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Eightth(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Nineth(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Tenth(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Eleventh(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Twelveth(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def pressing(self, instance):
        print(instance.text)
        self.manager.current = 'first'


class Lab4(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main(name='first'))
        sm.add_widget(Second(name='second'))
        sm.add_widget(Third(name='third'))
        sm.add_widget(Fourth(name='fourth'))
        sm.add_widget(Fiveth(name="fiveth"))
        sm.add_widget(Sixth(name="sixth"))
        sm.add_widget(Seventh(name="seventh"))
        sm.add_widget(Eightth(name="eightth"))
        sm.add_widget(Nineth(name="nineth"))
        sm.add_widget(Tenth(name="tenth"))
        sm.add_widget(Eleventh(name="eleventh"))
        sm.add_widget(Twelveth(name="twelveth"))
        return sm


if __name__ == "__main__":
    Lab4().run()