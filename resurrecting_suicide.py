

class ResurrectingSuicide:

    @classmethod
    def do(cls):

        from keyboard import is_pressed
        from pyautogui import click, hold
        from time import sleep
        from random import randrange as between

        sleep(between(2, 4))

        click(x=1380, y=661)

        check_count = between(14, 18)
        waiting_count = -1
        while not is_pressed('ctrl'):
            waiting_count += 1
            print(f'Waiting: {check_count - waiting_count}')
            if waiting_count == check_count:
                break
            sleep(1)

        with hold('r'):
            sleep(between(2, 4))