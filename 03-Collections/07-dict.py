'''
    >> Dictionary : Collection in python that can have elements in key and value pair

    representation : {}
    in-built class : dict()

    >> characteristics :

        - mutable
        - iterable
        - common naming convention for dict keys is string or int
        - dict keys are unique
        - values can duplicate/repeat or belong to other data type
'''

# black declaration:

di1={}
di2=dict()

print(type(di1),type(di2))

# initialization

di1={"a1":1,"a2":2,"a3":3}
print(di1)

# mutable

di2={"name":"Tirth",
     "age":18,
     "email":"abc@gmail.com",
     "address":"xyz"}

print("Name before: ",di2["name"])

di2["name"]="Abc"
print("Name after: ",di2["name"])

# get - to display the value of the given key

print(di2.get("name"))

# iterable

# .keys(): return key only (default)
# .values() : return value only
# .items() : return key value pair

for i in di2:
    print("Keys only:",i)

for i in di2.values():
    print("Values only:",i)

for k,v in di2.items():
    print(f"Key: {k} | Value: {v}")


