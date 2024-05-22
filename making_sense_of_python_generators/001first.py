def myfunc():
    return 1
    return 2
    return 3



def mygen():
    yield 1
    yield 2
    yield 3


func = myfunc()

gen = mygen()

next(gen)
next(gen)
next(gen)


next(func) # gonna raise error dude