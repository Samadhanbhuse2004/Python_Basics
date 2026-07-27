class Myclass:
    def __init__(self):
        pass

    @staticmethod
    def addition(a,b):
        return a+b
    
obj = Myclass()

print(obj.addition(10,23))

print(Myclass.addition(43,12))