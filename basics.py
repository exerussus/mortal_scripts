

class Resting:

    @classmethod
    def do(cls, count):
        from keyboard import is_pressed
        from pyautogui import press
        from time import sleep
        from random import uniform as between
        count += 1
        press('0')
        check_count = round(between((count - 1), (count + 1)))
        rest_count = 0
        while not is_pressed('ctrl'):
            rest_count += 1
            print(f'Resting seconds:  {check_count - rest_count}')

            if check_count <= rest_count:
                break
            sleep(1)

    @classmethod
    def normal(cls):
        return 30

    @classmethod
    def advance(cls):
        return "Resting count (normal = 30):  "


class Spurt:

    @classmethod
    def do(cls, rep):
        from keyboard import is_pressed
        from pyautogui import press, hold
        from time import sleep
        from random import uniform as between

        spurt_count = 0
        while not is_pressed('ctrl'):

            spurt_count += 1
            print(f'Remaining spurt cycles:  {rep - spurt_count}')
            if spurt_count == rep:
                break

            with hold('alt'):
                press('1')
            sleep(between(1.7, 2.2))
            press('q')
            sleep(between(1.0, 1.5))

    @classmethod
    def normal(cls):
        return 30

    @classmethod
    def advance(cls):
        return "Spurt's count (normal = 30):  "


class Waiting:

    @classmethod
    def do(cls, count):

        from keyboard import is_pressed
        from time import sleep
        from random import randrange as between
        check_count = between(count - 2, count + 2)
        waiting_count = -1
        while not is_pressed('ctrl'):
            waiting_count += 1
            print(f'Waiting: {check_count - waiting_count}')
            if waiting_count == check_count:
                break
            sleep(1)

    @classmethod
    def normal(cls):
        return 16

    @classmethod
    def advance(cls):
        return "Waiting seconds count (normal = 16):  "


class TimerCount:

    """Simple countdown.\n
    arg - seconds to wait"""

    def __init__(self):
        pass

    @staticmethod
    def countdown(sec=30):
        from keyboard import is_pressed
        from time import sleep

        print(f'Start after {sec} seconds. Press "p" to skip...')
        seconds = sec
        count = -1
        while not is_pressed('p'):

            seconds -= 1
            count += 1
            if sec == count:
                break

            print(seconds)
            sleep(1)


class LesserHeal:

    @classmethod
    def do(cls, rep):

        from keyboard import is_pressed
        from pyautogui import press, hold
        from time import sleep
        from random import uniform as between

        heal_count = 0
        while not is_pressed('ctrl'):

            heal_count += 1
            print(f'Remaining healing cycles:  {rep - heal_count}')
            if heal_count == rep:
                print('Done.')
                break
            with hold('alt'):
                press('4')
            sleep(between(1.7, 2.2))
            press('q')

    @classmethod
    def normal(cls):
        return 6

    @classmethod
    def advance(cls):
        return "Lesser heal count (normal = 6):  "


class Riding:

    @classmethod
    def do(cls, rep):

        from keyboard import is_pressed
        from time import sleep
        from pyautogui import hold

        with hold('w'):
            sleep(0.1)
        with hold('w'):
            sleep(0.1)

        count = -1
        while not is_pressed('ctrl'):

            count += 1
            if count == rep * 60:
                break

            with hold('a'):
                sleep(1)

    @classmethod
    def normal(cls):
        return 30

    @classmethod
    def advance(cls):
        return "Minutes count (normal = 30):  "