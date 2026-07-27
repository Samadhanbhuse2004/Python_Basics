class MyIntro:
    def get_name(self,name):
        return f"my name is {name}"
    
    def get_surname(self,surname):
        return f"surname is {surname}"
    
obj = MyIntro()
print(obj.get_name("Samadhan"))
print(obj.get_surname("Bhuse"))
