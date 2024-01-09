# open the file for writing
file=open('data1.txt','w')

# writable() : checks if the file is writable
print("Is this file in write mode :",file.writable())

# writing in file
file.write("Hello\n")

file.write("How are you Doing?\n")

# writing multiple string in file
li=["This is a car\n","Jack is dancing\n","Tom went grocery shopping nearby\n"]
file.writelines(li)

file.close()