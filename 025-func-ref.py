def lesen():
    print('schmoeker')

def essen():
    print('mjam')

todos = {
    'buch': lesen,
    'obst': essen,
    }
    
todo = input('was tun? ')
todos[todo]()