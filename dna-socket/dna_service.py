from dna import dna
import threading
import time
class DynamicVariable:
    def __init__(self, initial_value):
        self.value = initial_value

    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value

def function_with_dynamic_var(func, dynamic_var):
    def wrapper():
        while True:
            func(dynamic_var)
            # time.sleep(1)
    
    t = threading.Thread(target=wrapper)
    t.start()
    return t

def stop_thread(thread):
    thread.stop_thread = True
    thread.join()

# dynamic_var = DynamicVariable(('aa','aa'))

# t = function_with_dynamic_var(dna, dynamic_var)


# time.sleep(3)
# dynamic_var.set_value(("ccc", "ccc"))

# time.sleep(3)
# dynamic_var.set_value(("vvv","vvv"))

# stop_thread(t)