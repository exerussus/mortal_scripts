

class MountedMagery:

    """Special mounted training with water.\n
            You need to set "spurt" into 1 cell and
            "lesser heal" into 4 cell before using this
            script. Don't forget to get calamine and water.\n
            Mount your horse before using script. \n
            Hold 'ctrl' to stop."""

    @classmethod
    def start(cls):

        from basics import TimerCount
        from constructor import Constructor
        from advanced_menu import AdvancedMenu
        from resurrecting_suicide import ResurrectingSuicide

        repetition = AdvancedMenu.do()[0]
        if repetition == 0:
            pass
        else:
            TimerCount.countdown()
            Constructor.repetition(repetition, ResurrectingSuicide.do())
        TimerCount.countdown()

    @staticmethod
    def help_func():

        about = """
        Special mounted training with water.\n
        You need to set "spurt" into 1 cell and
        "lesser heal" into 4 cell before using this
        script. Don't forget to get calamine and water.\n
        Mount your horse before using script. \n
        Hold 'ctrl' to stop."""

        print(about)