class Bank:
    def __init__(self,name,acc_num,branch):
        self.__name = name
        self.__acc_num = acc_num
        self._branch = branch
    
    def statement(self):
        return f"The name of the account holder is : {self.__name} \nThe account number is : {self.__acc_num} \nBank branch is : {self._branch}"

b1 = Bank("Samadhan",'ac120495',"pune")

b1._Bank__acc_num
b1._Bank__name

print(b1.statement())