# Pizza and Pasta Menu with OOP

# contains all the products and pricing
class Product():
   def __init__(self):
      # menu pricing
      self.pizza=100
      self.pasta=50
      
      # total
      self.allTotal=0
      
      # pizza 
      self.pizzaSold=0
      self.pizzaTotal=0
      
      # pasta 
      self.pastaSold=0
      self.pastaTotal=0
      
      # extas
      self.softdrink=0
      self.bruschetta=0
      self.ice_cream=0
      
   def menu(self):
      print(f"""\n====================== Menu ======================
         
 1 Large Pizza = ₹{self.pizza} 

 2 Large Pizzas = ₹{self.pizza*2}

 3 Large Pizzas = ₹{self.pizza*3}

 ***Buy 4 or more Pizzas and get 1.5l of Soft Drink free***
 
--------------------------------

 1 large Pasta = ₹{self.pasta}

 2 Large Pastas = ₹{self.pasta*2}

 3 Large Pastas = ₹{self.pasta*3}

 ***Buy 4 or more Pastas and get 2 Bruschetta free.***

--------------------------------

 ***Buy 4 or more Pizzas and Pastas and get 2 Chocco Brownies Ice Cream free.***
 
--------------------------------\n""")

# contains all the calculation and billing data
class Bill(Product):
   def __init__(self):
      super().__init__()
      self.total=0
      
      # pizza
      self.pizzaNum=0
      self.pastaAmount=0
      
      # pasta
      self.pastaNum=0
      self.pastaAmount=0
   
   # order placing function
   def order(self):
      self.total=0
      
      self.orderPizza()
      self.orderPasta()
      self.special_offer()
         
      total=self.pizzaAmount+self.pastaAmount
      print(f"\nYour Total Order is: ₹{total}")
      self.allTotal+=total
      
      return self.allTotal
   
   def orderPizza(self):
      # pizza order
      self.pizzaNum=int(input("Enter no of Pizza you want : "))
      self.pizzaAmount=self.pizza*self.pizzaNum
      
      self.pizzaSold+=self.pizzaNum
      self.pizzaTotal+=self.pizzaAmount
      
      print(f"\nYour Pizza Order Amount is : ₹{self.pizzaAmount}")
      
      # pizza special offer
      if self.pizzaNum>3:
         self.softdrink+=1
         print("\n *** Congratulations !! 1.5lt Softdrink free *** ")
         
   def orderPasta(self):
       # pasta order
      self.pastaNum=int(input("\nEnter no of Pasta you want : "))
      self.pastaAmount=self.pasta*self.pastaNum
      
      self.pastaSold+=self.pastaNum
      self.pastaTotal+=self.pastaAmount
      
      print(f"\nYour Pasta Order Amount is : ₹{self.pastaAmount}")
      
      # pasta special offer
      if self.pastaNum>3:
         self.bruschetta+=1
         print("\n *** Congratulations !! Get 2 Bruschetta free ***  ")
   
   # combo special offer
   def special_offer(self):
      if self.pizzaNum>3 and self.pastaNum>3:
         self.ice_cream+=2
         print("\n *** Congratulations !! Get 2 Chocco Brownies Ice Cream free ***")
   
   # Shift summary with earnings and sellings
   def summary(self):
      print(f"""\n=========== Pizza and Pasta Bill ===========

 Payment received from Pizza :  ₹{self.pizzaTotal}

 Payment received from Pasta :  ₹{self.pastaTotal}

 Payment received today :  ₹{self.allTotal}

 Number of Pizza sold in one shift :  {self.pizzaSold}

 Number of Pasta sold in one shift :  {self.pastaSold}
 
 Number of 1.5lt Softdrink bottles given :  {self.softdrink}

 Number of Bruschetta given : {self.bruschetta}

 Number of Chocco Brownies Icecream given : {self.ice_cream}

 Bye Bye !!!""")
         
# object
bill=Bill()

# loop depandant
status=True

# shift start
print("""\n=========== Welcomme to Pizza and Pasta ===========
      
   press 1: order menu
   press 2: Exit\n""")
      
choice=int(input("Enter choice: "))
if choice!=1:
   status=False

# loop
while status:
   # menu printed to user
   bill.menu()
   
   # customer name
   name=input("Enter your name: ")
   print(f"\nWelcome, {name}\n")

   # total earnings of the day
   print(f"\n==>> Your Net Order Amount of the day is : ₹{bill.order()}")
   
   # for more customers
   more=input("\nDo you want to enter from another customer? [y/n] : ")
   
   if more=="Y" or more=="y":
      status=True
   else:
      status=False
      bill.summary()