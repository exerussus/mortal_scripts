def countdown(sec):
    from time import sleep

    for i in range(sec, 0, -1):
        print(i)
        sleep(1)


countdown(5)
