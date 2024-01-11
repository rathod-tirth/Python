# to control the pointer position inside the file we can use seek function

file=open('data.txt','r')

print(file.read())
file.seek(0) # position the pointer at the start
print(file.read())

file.close()