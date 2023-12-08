'''

    List : Collection that can store one or more value of diff. data type

    represents with : []
    inbuilt-class : list

    >>List Array Diff

    List is having multiple elements of multiple data types
    Array can have multiple elements of same data type

    >>Characteristics : 

        - Lists are mutable/changable
        - List support -ve indexing
        - List is orderable
        - Lists are iterable

'''

# blank list

li1=[]
li2=list()

print(type(li1))
print(type(li2))

li=[1,2,3,5.5,"Hello",'b',True,-10]

print(li)

# indexible and negetive indexible

print("3rd Index value:",li[3])
print("Last Index value:",li[-1])

# mutable

print("Before 5th element:",li[5])
li[5]='a'
print("After 5th element:",li[5])

# iterable

for i in li:
    print(i)













