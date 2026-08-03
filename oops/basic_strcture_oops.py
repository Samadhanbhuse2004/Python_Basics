class Car:
    wheels = 4
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        self.__mileage = 0
        
    def start(self):
        return f"{self.brand} {self.model} is starting"
    def get_mileage(self):
        return self.__mileage
    
    def drive(self,km):
        if km > 0:
            self.__mileage += km
            return f"Drove {km} km"  
        return "Invalid distance"
car1 = Car('BMW','X5',2022)
car2 = Car('Mercedes', 'C-Class', 2022)
print(car1.start())
print(car1.wheels)
print(car1.get_mileage())
  