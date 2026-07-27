class laptop:
    
    def __init__(self):
        self.brand = input("Please enter the laptop brand : ")
        
    def info(self):
        return f"Laptop is {self.brand} brand"
    
obj = laptop()

print(obj.info())