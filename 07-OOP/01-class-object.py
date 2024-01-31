'''
   OOP : Object Oriented Programming is a method of structuring a program by bundling related properties
   and behaviours into individual objects.
   
   Class : 
      - A class is a collection of objects.
      - It contains blueprint for the objects.
      - Class contains of member variable and member function
      - Members can be access throughout the class
      - A function in a class is usually denoted as method
      
   - Class method must have an extra first parameter in the method defination.
   - Python provides the parameter we do not have to specify it.
   - This works similar to pointer in C++
   
   Object :
      - Object is an instance of a class
      - object can access the class members using dot notations
'''

# class
class School:
   num=5 # member variable
   
   # self is the default class method parameter
   def myfun(self):   # member function / method
      return "hello"
   
# object
obj1=School()
print(obj1)

print("Num :",obj1.num)
print("Say",obj1.myfun())
