def myfunc():
    x = ''
    while True:
        print(f'Yielding x ({x}) and waiting...')
        x = yield
        if x is None:
            print('x is none')
            break
        print(f'Got x {x}. Doubling')
        x = x * 2



g = myfunc()
next(g)
# Yieldin x and waiting

g.send(10)
# Yielding x (20) and waiting...
# 20

g.send(123)
# Got x 123, doubling


g.send(None)
