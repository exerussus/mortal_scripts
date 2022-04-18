import pyautogui
import time
import keyboard
import threading


#
# # def trigger():
# #     pyautogui.press('q')
# #
# #
# # keyboard.add_hotkey('ctrl+shift', trigger)
#
# data_alt_key = {'key': ''}
#
#
# def press_block():
#     pass
#
#
# def key_watcher():
#     while keyboard.add_hotkey()
#     keyboard.add_hotkey('alt', press_block())
#     keyboard.wait('esc')
#
#
# thread_1 = threading.Thread(target=key_watcher)
# thread_2 = threading.Thread(target=alt_watcher)
# thread_1.start()
# thread_2.start()


def blocking():
    keyboard.press('n')


def pressing_key():
    while True:
        holding_key = keyboard.is_pressed('alt')
        if holding_key:
            blocking()

# def key_watcher():
#     keyboard.add_hotkey('alt', blocking(pressing_key()))
#     keyboard.wait('esc')
#
#
# thread_watcher = threading.Thread(target=key_watcher)
thread_pressing_key = threading.Thread(target=pressing_key)
# thread_watcher.start()
thread_pressing_key.start()
