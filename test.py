import pyautogui
import time

time.sleep(3)
x = 0
while True:
    pyautogui.move(0, 50)
    x += 1
    if x == 15:
        break


