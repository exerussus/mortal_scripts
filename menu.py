from swift_riding import *
from mental_training import *
from mounted_magery import *

def main_menu():
    while True:
        choice = input('Шо качаем?\n'
                       '1. Ментал тренинг\n'
                       '2. Маунтед мэджери\n'
                       '3. Свифт райдинг\n'
                       '0. Выход\n')
        if choice == '1':

            mental_training()
        if choice == '2':

            mounted_magery()
        if choice == '3':

            swift_riding()
        if choice == '0':
            input('Ня-пока...')
            exit(0)
