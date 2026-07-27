class MyIntro:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        
    def get_name(self):
        return f"Hello my name is: {self.name}"
    
    def get_surname(self):
        return f"surname is {self.surname}"
    
obj = MyIntro("Samadhan", "Bhuse")
print(obj.get_name()) 
print(obj.get_surname())          