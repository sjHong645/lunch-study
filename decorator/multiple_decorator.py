
def decorator1(func):
    def wrapper():
        print('Decorator 1')
        return func()
    return wrapper

def decorator2(func):
    def wrapper():
        print('Decorator 2')
        return func()
    return wrapper

@decorator1
@decorator2
def hello():
    print('Hello')
    
hello()