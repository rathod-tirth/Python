# Dunder / Magic Methods : This are special methods which are invoked on certain events

class School:
   # invokes automatically on object creation
   def __init__(self):
      self.num=10
      print("Hello")
      
   def display(self):
      return f"Num : {self.num}"
   
   # invokes automactically when class object is printed
   def __str__(self):
      return "School Object"
   
school=School()
print(school.display())
print(school)
