from pyautogui import click, hold
from random import randrange
from time import sleep


class MineLore:

    @staticmethod
    def suic_lore():
        while True:

            sleep(randrange(2, 4))

            click(x=1380, y=661)

            sleep(randrange(14, 18))

            with hold('r'):
                sleep(randrange(2, 4))


