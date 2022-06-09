

class SwiftRiding:

    """Special swift riding training.\n
            Mount your horse and use this script.\n
            That's all.\n
            P.S. Don't forget to feed your horse. Care about
            your horse. Sometimes it can save your mortal life.
             Hold 'ctrl' to stop."""

    @staticmethod
    def start():

        from basics import TimerCount, Riding
        from advanced_menu import AdvancedMenu
        from constructor import Constructor

        TimerCount.countdown()
        riding, repetition = AdvancedMenu.do(Riding)
        if repetition == 0:
            pass
        else:
            TimerCount.countdown()
            Constructor.repetition(repetition, Riding.do(riding))
        TimerCount.countdown()

    @staticmethod
    def help_func():

        about = """
        Special swift riding training.\n
        Mount your horse and use this script.\n
        That's all.\n
        P.S. Don't forget to feed your horse. Care about
        your horse. Sometimes it can save your mortal life.
         Hold 'ctrl' to stop."""

        print(about)
