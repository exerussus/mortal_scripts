

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