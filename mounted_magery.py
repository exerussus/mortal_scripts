

def aqau():
    import pyautogui
    import time
    import random

    data_first = [3.0, 3.2, 3.9, 3.1, 3.7, 3.8]
    data_second = [1.0, 1.2, 1.5, 1.1, 1.3, 1.4]

    pyautogui.press('1')
    time.sleep(random.choice(data_first))
    pyautogui.press('q')
    time.sleep(random.choice(data_second))


def heal():
    import pyautogui
    import time
    import random

    data_first = [3.0, 3.2, 3.9, 3.1, 3.7, 3.8]
    data_second = [1.0, 1.2, 1.5, 1.1, 1.3, 1.4]
    data_wait = [30, 35, 40, 45]

    pyautogui.press('4')
    time.sleep(random.choice(data_first))
    pyautogui.press('q')
    time.sleep(random.choice(data_second))


def mounted_magery():

    import time

    while True:
        time.sleep(3)
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        aqau()
        heal()
        heal()
        heal()
        heal()
        heal()
        heal()





