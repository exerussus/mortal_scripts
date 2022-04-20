from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config


Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 600)
Config.set('graphics', 'height', 400)
Config.write()


class MO2ScriptsApp(App):

    def mental(self, instance):
        from mental_training import mental_training
        mental_training()

    def magery(self, instance):
        from mounted_magery import mounted_magery
        mounted_magery()

    def build(self):
        bl = BoxLayout(orientation='vertical', padding=5)
        bl.add_widget(Button(text='Ментал трэйнинг', on_press=self.mental))
        bl.add_widget(Button(text='Маунтед мэджери', on_press=self.mental))
        bl.add_widget(Button(text='Свифт райдинг', on_press=self.mental))
        return bl


def do(): MO2ScriptsApp().run()


