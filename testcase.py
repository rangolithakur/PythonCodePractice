class Test():
    def __init__(self):
        print('test class called')
        
class OverloadingOperation(obect):
    def __init__(self, a, b):
        self.a = a
        self.b = b
		
    def __add__(self, a, b):
        print('inside add method')
        print(a,b)
        if type(a)==type(class) and type(b)==type(class):
            return a+b

if __name__ == "__main__":
    i = Test()
    j = Test()
    res = OverloadingOperation(i+j)
    print(res)
        
