def swift_riding():
    from pyautogui import press, hold
    import time

    time.sleep(3)
    press('w')
    time.sleep(0.2)
    press('w')
    with hold('a'):
        while True:
            pass
