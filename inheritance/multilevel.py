class Class1:
    def method1(self):
        return f"Class 1 method called"

class Class2(Class1):
    def method2(self):
        return f"Class 2 method called"
    
class Class3(Class2):
    def method3(self):
        return f"Class 3 method called"
    
class Class4(Class3):
    def method4(self):
        return f"Class 4 method called"
    
obj = Class4()

print(obj.method1())
print(obj.method2())
print(obj.method3())
print(obj.method4())