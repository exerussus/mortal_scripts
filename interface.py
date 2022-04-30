# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from kivy.config import Config
# from classes import Training
# from kivy.clock import mainthread
# from threading import Thread
#
# Config.set('graphics', 'resizable', 0)
# Config.set('graphics', 'width', 600)
# Config.set('graphics', 'height', 400)
# Config.write()
#
#
# class MO2ScriptsApp(App):
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.lbl = Label(text='Choose action', font_size=40)
#         self.key_action = ()
#
#     def build(self):
#         bl = BoxLayout(orientation='vertical', padding=25, spacing=25)
#         bl.add_widget(self.lbl)
#         bl.add_widget(Button(text='Mental training', font_size=25, on_press=self.pressed_button))
#         bl.add_widget(Button(text='Mounted magery', font_size=25,  on_press=self.pressed_button))
#         bl.add_widget(Button(text='Swift riding', font_size=25,  on_press=self.pressed_button))
#         bl.add_widget(Button(text='Human lore', font_size=25, on_press=self.pressed_button))
#         bl.add_widget(Button(text='Exit', font_size=25, on_press=self.pressed_button))
#         return bl
#
#     def update_lbl(self, text):
#         self.lbl.text = text
#
#     def pressed_button(self, instance):
#         self.key_action = instance.text
#
#         return 'Working'
#
#     def mental_training_button(self):
#
#         return Training.mental_training()
#
#     def mounted_magery_button(self):
#
#         return Training.mounted_magery()
#
#     def swift_riding_button(self):
#
#         return Training.swift_riding()
#
#     def human_lore_button(self):
#
#         return Training.human_lore()
#
#     def exit_button(self):
#         exit(0)
#
#     @mainthread
#     def threading_scripts(self):
#         from time import sleep
#         sleep(1)
#         print('Поток работает')
#
#         while True:
#
#             if self.key_action == 'Mental training':
#                 self.mental_training_button()
#                 self.key_action = 'None'
#
#             if self.key_action == 'Mounted magery':
#                 self.mounted_magery_button()
#                 self.key_action = 'None'
#
#             if self.key_action == 'Swift riding':
#                 self.swift_riding_button()
#                 self.key_action = 'None'
#
#             if self.key_action == 'Human lore':
#                 self.human_lore_button()
#                 self.key_action = 'None'
#
#             if self.key_action == 'Exit':
#                 self.exit_button()
#
#     def gui_activity(self):
#         t1 = Thread(target=self.threading_scripts)
#         # t2 = Thread(target=self.run())
#         t1.start()
#         # t2.start()

