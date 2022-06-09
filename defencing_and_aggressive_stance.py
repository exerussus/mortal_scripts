

class DefencingAndAggressiveStance:

    """Aggressive and defencing stance training.\n
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
        from basics import TimerCount

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
