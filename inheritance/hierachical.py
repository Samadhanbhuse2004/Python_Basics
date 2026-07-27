class A:
    def method1(self):
        return f"Class A method called"
    
class B(A):
    pass

class C(A):
    pass

obj = C()
print(obj.method1())