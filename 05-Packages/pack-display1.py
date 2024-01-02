# importing from package
import Package2.module1
from Package2.module1 import hello

num=int(input("Enter a num : "))

print("Factorial of that number :", Package2.module1.fact(num))

hello()
