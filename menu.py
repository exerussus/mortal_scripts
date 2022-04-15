

def main_menu():
    while True:
        choice = input('Шо качаем?\n'
                       '1. Ментал тренинг\n'
                       '0. Выход\n')
        if choice == '1':
            from mental_training import mental_training
            mental_training()
        if choice == '0':
            input('Ня-пока...')
            exit(0)
