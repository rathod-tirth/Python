# open() - To open the file

# opening the file in read mode
f = open("data.txt", 'r')
print(f.read())

# remember to close the file you have opened
f.close()

# opening the file using with statement
# with statement automatically closes the file once the block of code is executed.
with open("data.txt",'r') as f:
   data=f.read()
   print(data)

