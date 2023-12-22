'''
    Zip():
    
    - The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator
      is paired together, and then the second item in each passed iterator are paired together etc.

    - If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator.

'''

# zip()

li1=[5,10,36,78,42,1,91]
li2=[61,25,14,87,75,101]

zip1=zip(li1,li2)

print(list(zip1))

# unzip()

zip1=zip(li1,li2)

a,b=zip(*zip1)

print(a,b)
