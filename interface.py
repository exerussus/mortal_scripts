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
        sleep(1)
        instance.text = '3'
        sleep(1)
        instance.text = '2'
        sleep(1)
        instance.text = '1'
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

    def mental_training(self):
        import pyautogui
        import time
        import random

        data_first = [2.0, 2.2, 1.9, 2.1, 1.7, 1.8]
        data_second = [1.0, 1.2, 1.5, 1.1, 1.3, 1.4]
        data_wait = [30, 35, 20, 25]
        while True:
            pyautogui.press('1')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('q')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('4')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('4')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('4')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('4')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('4')
            time.sleep(random.uniform(1.7, 2.2))
            pyautogui.press('q')
            time.sleep(random.uniform(1.0, 1.5))
            pyautogui.press('0')
            time.sleep(random.uniform(24.0, 35.5))

def do(): MO2ScriptsApp().run()


