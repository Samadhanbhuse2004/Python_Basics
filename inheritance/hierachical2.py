class Father:
    def method1(self):
        return f"Father method called"
    
class Son(Father):
    pass

class Daughter(Father):
    pass

obj = Daughter()

obj1 = Son()

print(obj.method1())

print(obj1.method1())