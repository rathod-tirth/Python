# string functions

str1="helLo, (0w0) hAvE a 69 NiCe dAy 00 "

# capitalize : first character capital of the string
print(str1.capitalize())

# caseless/ all lowercase
print(str1.casefold())

# center
print(str1.center(50,"$"))

# count : return duplication of substring
print("No. of e in the string:",str1.casefold().count("e",13,27))

# endswith
print("Does the string ends with '.' :",str1.endswith("."))

# find
print("Index of letter l:",str1.find("l"))

# alphanumeric
print("Is the string alphanumeric:",str1.isalnum())

# split
print(str1.split(" "))

# title : first character capital of the word
print(str1.title())

