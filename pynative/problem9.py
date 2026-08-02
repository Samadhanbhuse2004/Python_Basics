vowel = ['a', 'e', 'i', 'o', 'u']
string = input("Enter a string: ")
count = 0
for char in string:
    if char.lower() in vowel:
        count += 1
print(f"Total vowels found: {count}")