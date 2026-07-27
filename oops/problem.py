class Animal:
    def __init__(self):
        self.name = input("Enter the Animal name : ")
        
    def get_animal(self):
        return f"Entered Animal name is : {self.name} "
obj = Animal()
print(obj.get_animal())