class Trace : 
    def __init__(self, func) : 
        self.func = func 

    def __call__(self, *args, **kwargs) : 
        r = self.func(*args, **kwargs)

        # 매개변수와 반환값 출력
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
                                            
        # self.func의 반환값을 반환
        return r                            

@Trace    
def add(a, b):
    return a + b
 
print(add(10, 20))
print(add(a=10, b=20))