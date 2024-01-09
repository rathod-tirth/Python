# readlines() : returns each line as a list element
file=open('data.txt','r')

read=file.readlines()
print("Readlines :",read)

file.close()

# readline() : returns single line as string
file=open('data.txt','r')

read=file.readline()
print("Readline :",read)

file.close()

# you can pass one argument in both of these functions to specify the length of the string the pointer has to cover