'''keys = ["name", "age", "city"] 
values = ["Bob", 25, "London"]
d1={}
for i in range(len(keys)):
    d1[keys[i]] = values[i]
print(d1)'''

'''l1 = [4,5,2,7,1,3]
l = len(l1)
print(l//2)'''
num = int(input("enter a num :"))
rev = 0
while num >0:
   rev = rev * 10 + num % 10
   num = num // 10 
    
print(rev)