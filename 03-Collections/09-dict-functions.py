# list-functions

di1={"name":"Abc",
     "email":"xyz@gmail.com",
     "age":89}
print("Before:",di1)

# update: update dict to the latest values

di2={"email":"abc@gmail.com","phone":"00XX-55XX-XX99"}
di1.update(di2)

print("After:",di1)

# pop: removes elements

di1.pop("age")

print("After pop:",di1)

# popitem: remvoes last elements

di1.popitem()
print("After popitem:",di1)

# copy: copies the dict

di3={}
di3=di1.copy()
print("After copy:",di3)

# clear: clears the dict

di1.clear()
print("Dict clear:",di1)
