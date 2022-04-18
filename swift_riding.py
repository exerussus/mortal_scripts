def swift_riding():
    from pyautogui import press, hold
    from time import sleep

    sleep(3)
    press('w')
    sleep(0.2)
    press('w')
    with hold('a'):
        while True:
            pass