class Mobile:
    def __init__(self):
        self.budget = int(input("What is your budget : "))
        self.color = input("Enter mobile color : ")
        self.ram = int(input("Enter the ram : "))
        self.rom = int(input("Enter the rom : "))
        
    def suggest_mobile(self):
        if self.budget == 15000:
            return f"you choose this mobile :  Realme"
        
        elif self.budget == 20000:
            return f"you choose this mobile : Vivo"
        elif self.budget == 25000:
            return f"you choose this mobile : Samsung"
        
        elif self.budget == 30000:
            return f"you choose this mobile : oneplus"
        elif self.budget == 150000:
            return f"you choose this mobile : iphone"
        else:
            return "sorry you not buy mobile "
        
    def mobile_color(self):
        return f"you choose color is : {self.color}"
    
    def  mobile_ram(self):
        return f"You choose ram is : {self.ram} GB"
    
    def mobile_rom(self):
        return f"You choose rom is : {self.rom} GB"
    
obj = Mobile()

print(obj.suggest_mobile())
print(obj.mobile_color())
print(obj.mobile_ram())
print(obj.mobile_rom())   