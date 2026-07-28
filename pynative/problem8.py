class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        print(f"Vehicle Name:  {self.name} \n Max Speed: {self.max_speed} \n Mileage: {self.mileage}" )
vehicle1 = vehicle("mercedes", 200, 10)