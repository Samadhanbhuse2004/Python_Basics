class Car:
    
    def __init__(self):
        
        self.color = input("Enter car color : ")
        
        self.brand = input("Enter car brand : ") 
        
        self.year = int(input("Enter car year : ")) 
        
        self.price = int(input("Enter car price : ")) 
    
    def car_color(self):
        return f"The car color is : {self.color}"
    
    def car_brand(self):
        return f"The car brand is : {self.brand}"
    
    def car_year(self):
        return f"The car year is : {self.year}"
    
    def car_price(self):
        return f"The car price is : {self.price}"
    
obj = Car()

print(obj.car_color())

print(obj.car_brand())

print(obj.car_year())

print(obj.car_price())       