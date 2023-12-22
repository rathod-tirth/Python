# string

name="John"
age=30

print("Name : "+name)

# f string

print(f"My name is {name} and my age is {age}")

print("My name is {1} and my age is {0}".format(age,name))

# end

print(f"My name is {name}",end=" & ")
print(f"My age is {age}")

# sep

print(name,age, sep="-")
