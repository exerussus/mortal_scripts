from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from time import sleep

from mounted_magery import mounted_magery
from swift_riding import swift_riding


Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 600)
Config.set('graphics', 'height', 400)
Config.write()


class MO2ScriptsApp(App):

    def mental(self, instance):

        instance.text = 'Процесс пошёл...'
        for i in range(1, 4):
            sleep(1)

        self.mental_training()

    def magery(self, instance):

        instance.text = 'Процесс пошёл...'
        sleep(1)
        instance.text = '3'
        sleep(1)
        instance.text = '2'
        sleep(1)
        instance.text = '1'
        sleep(1)
        mounted_magery()

    def swift(self, instance):

        instance.text = 'Процесс пошёл...'
        sleep(1)
        instance.text = '3'
        sleep(1)
        instance.text = '2'
        sleep(1)
        instance.text = '1'
        sleep(1)
        swift_riding()


    def build(self):
        bl = BoxLayout(orientation='vertical', padding=25, spacing=25)
        bl.add_widget(Button(text='Ментал трэйнинг', font_size=25, on_press=self.mental))
        bl.add_widget(Button(text='Маунтед мэджери', font_size=25,  on_press=self.magery))
        bl.add_widget(Button(text='Свифт райдинг', font_size=25,  on_press=self.swift))
        return bl





