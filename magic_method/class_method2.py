class College:
    cls_roll_no = 12
    def __init__(self,roll):
        self.roll = roll
        
    def get_val(self):
        return self.cls_roll_no
    
    @classmethod
    def set_val(cls, val):
        cls.cls_roll_no = val
        return cls.cls_roll_no  

obj = College(3)
print(obj.get_val())   
obj.set_val(10)        
print(obj.get_val())   
        