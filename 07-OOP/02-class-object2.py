# Can access and modify class member using the self parameter

class Calc:
   num1=0
   num2=0
   
   def input(self):
      num1=int(input("Enter Num 1 : "))
      num2=int(input("Enter Num 2 : "))
      self.num1,self.num2=num1,num2
   
   def add(self):
      return self.num1+self.num2

   def multi(self):
      return self.num1*self.num2
   
calc=Calc()
calc.input()
print("Addition :",calc.add())
print("Multiplication :",calc.multi())