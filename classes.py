import keyboard


class MentalOffence:

    """Special mental training with water.\n
        You need to set "spurt" into 1 cell and
        "lesser heal" into 4 cell before using this
        script. Don't forget to get calamine and water.\n
        Hold 'ctrl' to stop."""

    @staticmethod
    def start(repetition=10):

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
    def help_func():
        about = """
        Special mental training with water.\n
        You need to set "spurt" into 1 cell and
        "lesser heal" into 4 cell before using this
        script. Don't forget to get calamine and water.\n
        Hold 'ctrl' to stop."""

        print(about)


class HumanLore:

    """Special human lore training.\n
            Open character's menu (C key) and
            set your character facing to priest.
            After the cycles you have indicated,
            pick up the bags and cook all of that.\n
            P.S. set your window size at 1920 and 1080.\n
            Hold 'ctrl' to stop."""

    @staticmethod
    def start(repetition=20):

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
    def help_func():
        about = """
        Special human lore training.\n
        Open character's menu (C key) and
        set your character facing to priest.
        After the cycles you have indicated,
        pick up the bags and cook all of that.\n
        P.S. set your window size at 1920 and 1080.\n
        Hold 'ctrl' to stop."""

        print(about)


class MountedMagery:

    """Special mounted training with water.\n
            You need to set "spurt" into 1 cell and
            "lesser heal" into 4 cell before using this
            script. Don't forget to get calamine and water.\n
            Mount your horse before using script. \n
            Hold 'ctrl' to stop."""

    @staticmethod
    def start(repetition=10):

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
    def help_func():

        about = """
        Special mounted training with water.\n
        You need to set "spurt" into 1 cell and
        "lesser heal" into 4 cell before using this
        script. Don't forget to get calamine and water.\n
        Mount your horse before using script. \n
        Hold 'ctrl' to stop."""

        print(about)


class SwiftRiding:

    """Special swift riding training.\n
            Mount your horse and use this script.\n
            That's all.\n
            P.S. Don't forget to feed your horse. Care about
            your horse. Sometimes it can save your mortal life.
             Hold 'ctrl' to stop."""

    @staticmethod
    def start(minutes=30):

        from pyautogui import hold
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
    def help_func():

        about = """
        Special swift riding training.\n
        Mount your horse and use this script.\n
        That's all.\n
        P.S. Don't forget to feed your horse. Care about
        your horse. Sometimes it can save your mortal life.
         Hold 'ctrl' to stop."""

        print(about)


class BlockingTraining:
    """Special blocking training.\n
            This training not for your actions skills, It's for your
            mate. Set your character where you want and start the script.
            You will auto-attack and your mate will block.\n
             Before using:\n
            1.Set your settings overhead attack on 'alt' key and
            thrust attack on 'F' key. \n
            2.Put your swords on hotkeys 1, 2, 3... 9.\n
            After scripts starting choose speed of attack where 1 is very quickly,
            2 is normal and 3 is very slow.  Hold 'ctrl' to stop."""

    @staticmethod
    def start(repetitions=2, speed=None):

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

    @staticmethod
    def help_func():

        about = """
        Special blocking training.\n
        This training not for your actions skills, It's for your
        mate. Set your character where you want and start the script.
        You will auto-attack and your mate will block.\n
         Before using:\n
        1.Set your settings overhead attack on 'alt' key and
        thrust attack on 'F' key. \n
        2.Put your swords on hotkeys 1, 2, 3... 9.\n
        After scripts starting choose speed of attack where 1 is very quickly,
        2 is normal and 3 is very slow.  Hold 'ctrl' to stop."""

        print(about)


class DefencingAndAttackingStance:

    """Attacking and defencing stance training.\n
    Set your character facing to another character then
    start the script.
     Hold 'ctrl' to stop."""

    @staticmethod
    def start(repetitions=300):

        from pyautogui import click
        from time import sleep

        TimerCount.countdown(5)

        count = -1
        while not keyboard.is_pressed('ctrl'):

            count += 1
            if count == repetitions:
                break

            click()
            sleep(0.7)

    @staticmethod
    def help_func():

        about = """
        Attacking and defencing stance training.\n
        Set your character facing to another character then 
        start the script.\n Hold 'ctrl' to stop."""

        print(about)


class TimerCount:

    @staticmethod
    def countdown(sec):

        from time import sleep

        for i in range(sec, 0, -1):
            print(i)
            sleep(1)


class ConsoleBuild:

    def __init__(self):
        pass

    @staticmethod
    def run():
        from time import sleep
        print('Welcome to MO2 scripts!')
        sleep(0.2)

        while not keyboard.is_pressed('0'):

            choice = input('Choose action script:\n'
                           '1. Mental training\n'
                           '2. Mounted magery\n'
                           '3. Human lore\n'
                           '4. Swift riding\n'
                           '5. Blocking training\n'
                           '6. Defencing and attacking stance\n'
                           '0. Exit \n'
                           'If you need help, write "h" after number.'
                           'Your choice: ')

            if choice == '1':
                MentalOffence.start()
            elif choice == '2':
                MountedMagery.start()
            elif choice == '3':
                HumanLore.start()
            elif choice == '4':
                SwiftRiding.start()
            elif choice == '5':
                BlockingTraining.start()
            elif choice == '6':
                DefencingAndAttackingStance.start()
            elif choice == '0':
                exit(0)

            elif choice == '1h':
                MentalOffence.help_func()
                input('Press any key...')
            elif choice == '2h':
                MountedMagery.help_func()
                input('Press any key...')
            elif choice == '3h':
                HumanLore.help_func()
                input('Press any key...')
            elif choice == '4h':
                SwiftRiding.help_func()
                input('Press any key...')
            elif choice == '5h':
                BlockingTraining.help_func()
                input('Press any key...')
            elif choice == '6h':
                DefencingAndAttackingStance.help_func()
                input('Press any key...')
            else:
                print('Please choose number from list...')

                sleep(0.2)
