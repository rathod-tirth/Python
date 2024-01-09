# open() - To open the file

# the open function takes 2 args : 1. filename, 2. mode
f = open("data.txt", 'r')
print(f.read())

# remember to close the file you have opened
f.close()
