
class TimeActions:

    def __init__(self):
        pass

    @staticmethod
    def countdown(seconds):
        from time import sleep
        for i in range(seconds, 0, -1):
            print(str(f'До старта {i} сек...'))
            sleep(1)
        print('Работает')


class Training:

    def __init__(self):
        pass

    @staticmethod
    def mental_training(repetition=10):

        """Special mental training with water.\n
        You need to set "spurt" into 1 cell and
        "lesser heal" into 4 cell before using this
        script. Don't forget to get calamine and water."""

        from pyautogui import press
        from time import sleep
        from random import uniform as between

        TimeActions.countdown(3)

        for rep in range(repetition):

            for i in range(50):
                press('1')
                sleep(between(1.7, 2.2))
                press('q')
                sleep(between(1.0, 1.5))

            for i in range(5):
                press('4')
                sleep(between(1.7, 2.2))
                press('q')

            press('0')
            sleep(between(24.0, 35.5))

    @staticmethod
    def human_lore(repetition=20):

        """Special human lore training.\n
        Open character's menu (C key) and
        set your character facing to priest.
        After the cycles you have indicated,
        pick up the bags and cook all of that.\n
        P.S. set your window size at 1920 and 1080."""

        from pyautogui import click, hold
        from time import sleep
        from random import randrange as between

        TimeActions.countdown(3)

        for i in range(repetition):

            sleep(between(2, 4))

            click(x=1380, y=661)

            sleep(between(14, 18))

            with hold('r'):
                sleep(between(2, 4))

    @staticmethod
    def mounted_magery(repetition=10):

        """Special mounted training with water.\n
        You need to set "spurt" into 1 cell and
        "lesser heal" into 4 cell before using this
        script. Don't forget to get calamine and water.\n
        Mount your horse before using script. """

        from pyautogui import press
        from time import sleep
        from random import uniform as between

        for rep in range(repetition):
            for i in range(23):
                press('1')
                sleep(between(3, 4))
                press('q')
                sleep(between(1, 2))

            for i in range(6):
                press('4')
                sleep(between(3, 4))
                press('q')
                sleep(between(1, 2))


Training.human_lore()
