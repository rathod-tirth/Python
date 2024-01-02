# importing module from the same directory

import module1 # imports the whole module
from module1 import add,sub # individual objects
from module1 import mult as multiplication # named import
from module1 import * # imports everything

num1=int(input("Enter number 1 : "))
num2=int(input("Enter number 2 : "))

print("Addition :", add(num1,num2))
print("Subtraction :", sub(num1,num2))
print("Multiplication :", multiplication(num1,num2))
print("Number is :",even_odd(num1))
