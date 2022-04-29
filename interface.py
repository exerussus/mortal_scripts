from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from classes import Training


Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 600)
Config.set('graphics', 'height', 400)
Config.write()


class MO2ScriptsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lbl = Label(text='Choose action', font_size=40)

    def build(self):
        bl = BoxLayout(orientation='vertical', padding=25, spacing=25)
        self.lbl = Label(text='Choose action')
        bl.add_widget(self.lbl)
        bl.add_widget(Button(text='Mental training', font_size=25, on_press=self.mental_training_button))
        bl.add_widget(Button(text='Mounted magery', font_size=25,  on_press=self.mounted_magery_button))
        bl.add_widget(Button(text='Swift riding', font_size=25,  on_press=self.swift_riding_button))
        bl.add_widget(Button(text='Human lore', font_size=25, on_press=self.human_lore_button))
        bl.add_widget(Button(text='Exit', font_size=25, on_press=self.exit_button))
        return bl

    def update_lbl(self, text):
        self.lbl.text = text

    def countdown(self, seconds):
        from time import sleep
        for i in range(seconds, 0, -1):
            self.lbl.text = f'{i} sec...'
            sleep(1)

        return 'Working'

    def mental_training_button(self, instance):

        self.update_lbl(self.countdown(3))
        self.update_lbl(Training.mental_training())

    def mounted_magery_button(self, instance):

        self.update_lbl(self.countdown(3))
        self.update_lbl(Training.mounted_magery())

    def swift_riding_button(self, instance):

        self.update_lbl(self.countdown(3))
        self.update_lbl(Training.swift_riding())

    def human_lore_button(self, instance):

        self.update_lbl(self.countdown(3))
        self.update_lbl(Training.human_lore())

    def exit_button(self, instance):
        from time import sleep
        self.update_lbl('Thx for using this app')
        sleep(1)
        exit(0)


