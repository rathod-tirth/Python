# read : opening the file in readonly mode

f = open('data.txt', 'r')

# ways you can access the read mode file

read=f.read()
print(read)

# 1. loop
# for i in f:
#    print(i)

# 2. read(): in-built function which reads the whole file
f.close()

f = open('data.txt', 'r')

for i in f:
   print(i)

read=f.read()
print(read)

f.close()
