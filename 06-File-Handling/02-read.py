# opening the file in read mode
file = open('data.txt', 'r')

'''
To read the data we use in-built functions :
- read() : returns the entire file as string
- readlines() : returns each line as a list element
- readline() : returns a single line as string
'''

# read()
read=file.read()
print("Read 1 :",read)

# returns empty string
read2=file.read()
print("Read 2 :",read2)

'''
- Python uses pointer to operate on files.
- The pointer remembers the current position in the file 
and determines from where the next read operations will start from.
- Since the first read operation reads the entire file, the pointer is at the end of the file.
Now when the second read operation occurs there is nothing left to read so it returns an empty string.
'''

file.close()

# read function takes an one argument to specify how far does 
# the pointer has to travel and that will determine the length of the returing string 
file=open('data.txt','r')
read3=file.read(10)
print("Read 3 :",read3)