class Student:

    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks

    def get_marks(self):
        return f'the marks of a student are {self.__marks}'

    def set_marks(self,marks):
        self.__marks = marks


ob1 = Student("Jake",'100')


print(ob1.get_marks())

print(ob1.set_marks(95))

print(ob1.get_marks())