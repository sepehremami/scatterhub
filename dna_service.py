from dna import dna
import time
def run_dna():
    node = ''
    while True: 
        node = yield 
        yield from dna(node)



runner = run_dna()

next(runner)
# runner.send(None)
runner.send(('a', 'b'))
runner.send(None)
runner.send(('b', 'a'))
