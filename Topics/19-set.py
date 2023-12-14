'''
    set : A collection in python which can have mutiple type
            of mutltiple elements but doesn't support duplicate entry

    represents : {}
    in-built class : set()

    >> characteristics :
        - no duplication
        - not orderable
        - iterable
        - not indexible
        - immutable

'''

# blank declaration

s1={} # invalid
print(type(s1))

s2=set()
print(type(s2))

# no duplication

s2={5,10,5,3,3,1}

print(s2)
# not indexible or mutable since its not orderable

print(s2[1])

# iterable

for i in s2:
    print(i)






    
