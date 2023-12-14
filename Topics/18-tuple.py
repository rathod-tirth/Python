'''
    Tuple : Collection in python

    represents with : ()
    in-built class : tuple

    >> Characteristics :

        - immutable
        - orderable
        - indexible
        - iterable

    >> Differences between tuple and list:

        - list is mutable
        - tuple is immutable

'''

# blank declaration:

t1=()
t2=tuple()

print(type(t1),type(t2))

# initialization

t1=(1,2,3,"abc")
t2=5.5,8,"xyz"

print(t1,t2)

# remember to add a comma for single value tuple

t3=(5,)
print(type(t3))

# indexible

print(t1[3])

# iterable

for i in t1:
    print(i)












