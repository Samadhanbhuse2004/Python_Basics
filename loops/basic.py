str1 = 'The quick brown fox jumps over the lazy dog'
for i in str1:
    if i!=' ':
        print(f'the occurrence of {i} is {str1.count(i)}')

vowels = ['a','e','i','o','u']        
for i in str1:
    if i in vowels:
        print(f'the vowel {i} is at index {str1.index(i)}')