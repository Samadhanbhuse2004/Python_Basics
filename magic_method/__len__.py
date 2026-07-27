class Myclass:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return (self.x+other.x,self.y+other.y)

    def __mul__(self, other):
        return (self.x*other.x,self.y*other.y)
    
    def __len__(self):
        return 3


ob1 = Myclass(1,2)
ob2 = Myclass(3,4)

ob1+ob2
ob1*ob2

print(len(ob1))