import time

import keyboard


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

        TimerCount.countdown(5)

        count = -1
        while not keyboard.is_pressed('ctrl'):

            count += 1
            if count == repetition:
                break

            spurt_count = 0
            while not keyboard.is_pressed('ctrl'):

                spurt_count += 1
                if spurt_count == 50:
                    break

                press('1')
                sleep(between(1.7, 2.2))
                press('q')
                sleep(between(1.0, 1.5))

            heal_count = 0
            while not keyboard.is_pressed('ctrl'):

                heal_count += 1
                if heal_count == 6:
                    break

                press('4')
                sleep(between(1.7, 2.2))
                press('q')

            press('0')
            sleep(between(24.0, 35.5))

        return 'Done'

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

        TimerCount.countdown(5)

        count = -1
        while not keyboard.is_pressed('ctrl'):

            count += 1
            if count == repetition:
                break

            sleep(between(2, 4))

            click(x=1380, y=661)

            sleep(between(14, 18))

            with hold('r'):
                sleep(between(2, 4))

        return 'Done'

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

        TimerCount.countdown(5)

        count = -1
        while not keyboard.is_pressed('ctrl'):

            count += 1
            if count == repetition:
                break

            spurt_count = 0
            while not keyboard.is_pressed('ctrl'):
                spurt_count += 1
                press('1')
                sleep((between(3, 4)))
                press('q')
                sleep(between(1, 2))
                if spurt_count == 23:
                    break

            heal_count = 0
            while not keyboard.is_pressed('ctrl'):
                heal_count += 1
                press('4')
                sleep(between(3, 4))
                press('q')
                sleep(between(1, 2))
                if heal_count == 5:
                    break

        return 'Done'

    @staticmethod
    def swift_riding(minutes=30):

        """Special swift riding training.\n
        Mount your horse and use this script.\n
        That's all.\n
        P.S. Don't forget to feed your horse. Care about
        your horse. Sometimes it can save your mortal life."""

        from pyautogui import press, hold
        from time import sleep

        TimerCount.countdown(5)

        while not keyboard.is_pressed('ctrl'):

            with hold('w'):
                sleep(0.1)
            with hold('w'):
                sleep(0.1)
            with hold('a'):
                sleep(minutes * 60)

    @staticmethod
    def blocking_training(repetitions=2, speed=None):

        """Special blocking training.\n
        This training not for your actions skills, It's for your
        mate. Set your character where you want and start the script.
        You will auto-attack and your mate will block.\n
         Before using:\n
        1.Set your settings overhead attack on 'alt' key and
        thrust attack on 'F' key. \n
        2.Put your swords on hotkeys 1, 2, 3... 9.\n
        After scripts starting choose speed of attack where 1 is very quickly,
        2 is normal and 3 is very slow."""

        from pyautogui import click, press
        from time import sleep
        import random
        import keyboard

        if not speed:
            try:
                speed = int(input('Choose attack speed:\n'
                                  '1. Fast\n'
                                  '2. Medium\n'
                                  '3. Slow\n'
                                  'Your choice: '))
            except ValueError:
                speed = 1

        TimerCount.countdown(5)

        if speed == 1:
            actually_speed = 0.7
        elif speed == 2:
            actually_speed = 1.1
        else:
            actually_speed = 1.4

        change_sword = 0
        key_sword = 1
        cycles = 0

        while not keyboard.is_pressed('ctrl'):

            cycles += 1
            change_sword += 1

            attack = random.randrange(1, 5)

            if attack == 1:
                press('a')
                click()
                sleep(actually_speed)

            if attack == 2:
                press('d')
                click()
                sleep(actually_speed)

            if attack == 3:
                press('alt')
                sleep(actually_speed)

            if attack == 4:
                press('f')
                sleep(actually_speed)

            if change_sword == 90:
                if key_sword < 9:
                    press(str(key_sword))
                    key_sword += 1
                    change_sword = 0
            if repetitions == cycles:
                break


class TimerCount:

    @staticmethod
    def countdown(sec):

        from time import sleep

        for i in range(sec, 0, -1):
            print(i)
            sleep(1)


Training.blocking_training()
