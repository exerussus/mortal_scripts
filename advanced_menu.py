

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
            values_list.append(999)
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
