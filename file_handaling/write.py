with open ("/Users/samadhanbhuse/Desktop/python_basic/file_handaling/file2.txt",'w') as f:
    f.write("Hello how are you?")

with open("/Users/samadhanbhuse/Desktop/python_basic/file_handaling/file2.txt",'r') as f:
    content = f.read()
    print(content)