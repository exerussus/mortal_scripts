

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


class Resting:

    @classmethod
    def do(cls, count):
        from keyboard import is_pressed
        from pyautogui import press
        from time import sleep
        from random import uniform as between

        press('0')
        check_count = between((count - 5), (count + 5))
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


class Constructor:

    @classmethod
    def simple(cls, *args):

        for i in args:
            i

    @classmethod
    def repetition(cls, repetition, *args):
        from keyboard import is_pressed

        count = -1
        while not is_pressed('ctrl'):

            count += 1
            print(f'Remaining cycles:  {repetition - count}')
            if count == repetition:
                break

            for i in args:
                i


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


class Waiting:

    @classmethod
    def do(cls):

        from keyboard import is_pressed
        from time import sleep
        from random import randrange as between
        check_count = between(14, 18)
        waiting_count = -1
        while not is_pressed('ctrl'):
            waiting_count += 1
            print(f'Waiting: {check_count - waiting_count}')
            if waiting_count == check_count:
                break
            sleep(1)


class AdvancedMenu:

    @classmethod
    def do(cls, *args):
        setting_choice = input("Choose a setting:\n"
                               "1. Standard\n"
                               "2. Advanced\n"
                               "3. Back\n"
                               "Your choice: ")

        if setting_choice == '1':
            values_list = []
            for i in args:
                values_list.append(i.normal())
            return values_list

        elif setting_choice == '2':
            values_list = []
            for i in args:
                values_list.append(int(input(i.advance())))
            values_list.append(int(input('Cycles (normal = 25):  ')))
            return values_list

        elif setting_choice == '0':
            values_list = []
            for _ in args:
                values_list.append(0)
            return values_list

        else:
            input('Please choose number from list...')
            values_list = []
            for _ in args:
                values_list.append(0)
            return values_list


class MentalOffence:

    """Special mental training with water.\n
        You need to set "spurt" into alt+1 cell,
        "lesser heal" into alt+4 cell and resting into alt+9 before using this
        script. Don't forget to get calamine and water.\n
        Hold 'ctrl' to stop."""

    @classmethod
    def start(cls):
        spurt, lesser_heal, resting, repetition = AdvancedMenu.do(Spurt, LesserHeal, Resting)
        if spurt == 0 or lesser_heal == 0 or resting == 0 or repetition == 0:
            pass
        else:
            TimerCount.countdown()
            Constructor.repetition(repetition, Spurt.do(spurt), LesserHeal.do(lesser_heal), Resting.do(resting))

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

    @classmethod
    def start(cls):
        repetition = AdvancedMenu.do()[0]
        if repetition == 0:
            pass
        else:
            TimerCount.countdown()
            Constructor.repetition(repetition, ResurrectingSuicide.do())

    @classmethod
    def help_func(cls):
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

    @classmethod
    def start(cls):
        repetition = AdvancedMenu.do()[0]
        if repetition == 0:
            pass
        else:
            TimerCount.countdown()
            Constructor.repetition(repetition, ResurrectingSuicide.do())
        TimerCount.countdown()

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
        from keyboard import is_pressed
        from pyautogui import hold
        from time import sleep

        TimerCount.countdown()

        while not is_pressed('ctrl'):

            with hold('w'):
                sleep(0.1)
            with hold('w'):
                sleep(0.1)

            count = -1
            while not is_pressed('ctrl'):

                count += 1
                if count == minutes * 60:
                    break

                with hold('a'):
                    sleep(1)

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

        from keyboard import is_pressed
        from pyautogui import click, press
        from time import sleep
        import random

        if not speed:
            try:
                speed = int(input('Choose attack speed:\n'
                                  '1. Fast\n'
                                  '2. Medium\n'
                                  '3. Slow\n'
                                  'Your choice: '))
            except ValueError:
                speed = 1

        TimerCount.countdown()

        if speed == 1:
            actually_speed = 0.7
        elif speed == 2:
            actually_speed = 1.1
        else:
            actually_speed = 1.4

        change_sword = 0
        key_sword = 1
        cycles = 0

        while not is_pressed('ctrl'):

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

    def __init__(self):
        pass

    @staticmethod
    def start(repetitions=300):

        from keyboard import is_pressed
        from pyautogui import click
        from time import sleep

        TimerCount.countdown()

        count = -1
        while not is_pressed('ctrl'):

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


class AutoAttacker:

    """Simple attacking script.\n
    Set your character facing to another character\n
    and start this script to attack.\n
    Hold 'ctrl' to stop."""

    @staticmethod
    def start():
        from pyautogui import click
        from time import sleep
        from keyboard import is_pressed
        from random import uniform

        TimerCount.countdown()

        while not is_pressed('ctrl'):

            click()
            sleep(uniform(0.1, 0.3))

    @staticmethod
    def help_func():

        about = """Simple attacking script.\n
                Set your character facing to another character\n
                and start this script to attack.\n
                Hold 'ctrl' to stop."""

        print(about)


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


class ConsoleBuild:

    """Build of all training scripts."""

    def __init__(self):
        pass

    @staticmethod
    def run():

        from time import sleep
        print('Welcome to MO2 scripts!')
        sleep(0.2)

        while True:

            choice = input('Choose action script:\n'
                           '1. Mental training\n'
                           '2. Mounted magery\n'
                           '3. Human lore\n'
                           '4. Swift riding\n'
                           '5. Blocking training\n'
                           '6. Defencing and attacking stance\n'
                           '7. Auto-Attack\n'
                           '0. Exit \n'
                           'If you need help, write "h" after number.\n'
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
            elif choice == '7':
                AutoAttacker.start()
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
            elif choice == '7h':
                AutoAttacker.help_func()
                input('Press any key...')
            else:
                print('Please choose number from list...')

                sleep(0.2)
