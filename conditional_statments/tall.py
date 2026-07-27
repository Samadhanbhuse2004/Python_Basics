person1= int(input("enter the age of person1: "))
person2= int(input("enter the age of person2: "))
person3= int(input("enter the age of person3: "))
if person1 > person2 and person1 < person3:
    print("person1 is the tallest ")
elif person2 > person1 and person2 < person3:
    print("person2 is the tallest ")
else:
    print("person3 is the tallest ")
tall=max(person1,person2,person3)
map = { person1: "person1", person2: "person2", person3: "person3"}
print(map[tall])