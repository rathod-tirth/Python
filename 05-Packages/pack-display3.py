# importing everything from the package using the __all__
from Package import *

num=int(input("Enter a num : "))
print("Factorial of that number :", module1.fact(num))

module1.hello()

string=input("Enter a string : ")
print("Number of Words in the string :",module2.num_words(string))