class Myclass:

    cls_variable = 100

    def __init__(self,a,b):
        self.a = a
        self.b = b

    
    def get_var(self):
        return self.cls_variable
    
    @classmethod
    def set_var(cls,val):
        cls.cls_variable = val
    

o1 = Myclass(10,20)

print(o1.get_var())

print(o1.set_var(200))

print(o1.get_var())

o2 = Myclass(1,2)

print(o2.get_var())

print(o1.get_var())

o3 = Myclass(2,3)

print(o3.get_var())