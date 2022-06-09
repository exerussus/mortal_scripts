

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
        from basics import TimerCount

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
