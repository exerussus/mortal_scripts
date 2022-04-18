

def main_menu():
    while True:
        choice = input('Шо качаем?\n'
                       '1. Ментал тренинг\n'
                       '2. Маунтед мэджери\n'
                       '3. Свифт райдинг\n'
                       '0. Выход\n')
        if choice == '1':
            from mental_training import mental_training
            mental_training()
        if choice == '2':
            from mounted_magery import mounted_magery
            mounted_magery()
        if choice == '3':
            from swift_riding import swift_riding
            swift_riding()
        if choice == '0':
            input('Ня-пока...')
            exit(0)
