'''
    String in python

    - represents with : 'hello',"hello","""Hello"""
    - class : str
    - indexible (starts from 0)
    - mutable
    - iterable
    - supports -ve indexing (starts from -1)
    
'''

str1=''
str2=str()
str3=""
str4="""
                Essay

        1. First Point
        2. Second Point
        3. Third Point
        ...
"""

print(type(str1))
print(str4)


# isinstance(obj,class) returns boolean

print(isinstance(str1,str))
print(isinstance(55,str))

# length

print("Length of String:",len(str4))


# concate

s1="Hello"
s2="World"

print(s1+s2)

print(s1*5)

# index

sen="Hello have a nice day"

print("6th letter:",sen[6])

# reverse index

print("last letter:",sen[-1])






















