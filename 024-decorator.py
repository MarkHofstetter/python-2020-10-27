import time

'''
einen decorator namens "timing" zu schreiben, der die Laufzeit
einer funktion misst
'''

def demo_decorator(func_ref):
    def wrapper():
        print("vorher")
        func_ref()
        print("nachher")
    
    return wrapper
  

def timing(func_ref):
    def wrapper():
        t_start = time.time()
        func_ref()
        t_end = time.time()
        print("run time {:f}".format(t_end-t_start))
    return wrapper
    
@demo_decorator    
@timing
def my_function():
    print("do something")
    time.sleep(1)

if __name__ == "__main__":
    my_function()
    