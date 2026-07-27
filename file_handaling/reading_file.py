f = open("/Users/samadhanbhuse/Desktop/python_basic/file_handaling/file.txt",'r')

content = f.read()

print(content)

f.close()

with open("/Users/samadhanbhuse/Desktop/python_basic/file_handaling/file.txt",'r') as f:
    
    content = f.read()
    
    print(content)
    