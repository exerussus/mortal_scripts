

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
        from basics import TimerCount

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