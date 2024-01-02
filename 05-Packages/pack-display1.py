# importing from package
import Package.module1
from Package.module1 import hello

num=int(input("Enter a num : "))

print("Factorial of that number :", Package.module1.fact(num))

hello()
