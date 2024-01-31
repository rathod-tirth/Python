'''
   Inheritance : Inheritance is a concept that allows one class to derive or inherit another class.

   Types of Inheritance :
      1. Single
      2. Multiple
      3. Multi-level
      4. Hierarchical
      5. Hybrid
'''

class A:
   def display1(self):
      print("Hello from Class A")
   
class B(A):
   def display2(self):
      print("Hello from Class B")
      
obj=B()
obj.display1()
obj.display2()