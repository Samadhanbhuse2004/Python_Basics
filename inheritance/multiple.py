class Father:
    def property(self):
        return f"I have a house"
    
class Mother:
    def assets(self):
        return f"I have a car"
    
class Son(Father,Mother):
    pass

obj = Son()
print(obj.property())
print(obj.assets())    