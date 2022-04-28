

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
        """Special mental training with water.
        You need to set "spurt" into 1 cell and
        "lesser heal" into 4 cell before using this
        script. """
        from pyautogui import press
        from time import sleep
        from random import uniform as between

        TimeActions.countdown(3)

        for l in range(repetition):

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


Training.mental_training()