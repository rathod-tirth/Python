# open file in append
file=open('data1.txt','a')

# use the same write function to write on file
# but won't overwrite the existing data
file.write("\nFrom Append mode Hello!!")

file.close()