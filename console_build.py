

class ConsoleBuild:

    """Build of all training scripts."""

    def __init__(self):
        pass

    @staticmethod
    def run():
        from mental_offence import MentalOffence
        from auto_attacker import AutoAttacker
        from blocking_training import BlockingTraining
        from defencing_and_aggressive_stance import DefencingAndAggressiveStance
        from swift_riding import SwiftRiding
        from mounted_magery import MountedMagery
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
                pass
            elif choice == '4':
                SwiftRiding.start()
            elif choice == '5':
                BlockingTraining.start()
            elif choice == '6':
                DefencingAndAggressiveStance.start()
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
                pass
                input('Press any key...')
            elif choice == '4h':
                SwiftRiding.help_func()
                input('Press any key...')
            elif choice == '5h':
                BlockingTraining.help_func()
                input('Press any key...')
            elif choice == '6h':
                DefencingAndAggressiveStance.help_func()
                input('Press any key...')
            elif choice == '7h':
                AutoAttacker.help_func()
                input('Press any key...')
            else:
                print('Please choose number from list...')

                sleep(0.2)
