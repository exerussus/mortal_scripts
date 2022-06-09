

class MentalOffence:

    """Special mental training with water.\n
        You need to set "spurt" into alt+1 cell,
        "lesser heal" into alt+4 cell and resting into alt+9 before using this
        script. Don't forget to get calamine and water.\n
        Hold 'ctrl' to stop."""

    @classmethod
    def start(cls):
        from basics import Spurt, LesserHeal, Resting
        from advanced_menu import AdvancedMenu
        from basics import TimerCount
        from constructor import Constructor

        spurt, lesser_heal, resting, repetition = AdvancedMenu.do(Spurt, LesserHeal, Resting)
        if spurt == 0 or lesser_heal == 0 or resting == 0 or repetition == 0:
            pass
        else:
            TimerCount.countdown()
            Constructor.repetition(repetition, Spurt.do(spurt), LesserHeal.do(lesser_heal), Resting.do(resting))

    @staticmethod
    def help_func():
        about = """
        Special mental training with water.\n
        You need to set "spurt" into 1 cell and
        "lesser heal" into 4 cell before using this
        script. Don't forget to get calamine and water.\n
        Hold 'ctrl' to stop."""

        print(about)