

def mounted_magery():
    import pyautogui
    import time
    import random

    data_first = [3.0, 3.2, 3.9, 3.1, 3.7, 3.8]
    data_second = [1.0, 1.2, 1.5, 1.1, 1.3, 1.4]
    data_wait = [30, 35, 40, 45]
    while True:
        time.sleep(3)
        with pyautogui.hold('r'):
            time.sleep(2)


        pyautogui.press('1')
        time.sleep(random.choice(data_first))
        pyautogui.press('q')
        time.sleep(random.choice(data_second))


        x = 0
        while True:
            pyautogui.move(0, 50)
            x += 1
            if x == 15:
                break

        with pyautogui.hold('r'):
            time.sleep(2)

        time.sleep(random.choice(data_first))
        pyautogui.press('0')
        time.sleep(random.choice(data_wait))



mounted_magery()