# Pizza and Pasta Menu with OOP

class Menu():
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
   
   # order placing function
   def order(self):
      total=0
      
      # pizza order
      pizzaOrder=int(input("Enter no of Pizza you want : "))
      pizzaAmount=self.pizza*pizzaOrder
      total+=pizzaAmount
      
      self.pizzaSold+=pizzaOrder
      self.pizzaTotal+=pizzaAmount
      
      print(f"\nYour Pizza Order Amount is : ₹{pizzaAmount}")
      
      # pizza special offer
      if pizzaOrder>3:
         self.softdrink+=1
         print("\n *** Congratulations !! 1.5lt Softdrink free *** ")
      
      # pasta order
      pastaOrder=int(input("\nEnter no of Pasta you want : "))
      pastaAmount=self.pasta*pastaOrder
      total+=pastaAmount
      
      self.pastaSold+=pastaOrder
      self.pastaTotal+=pastaAmount
      
      print(f"\nYour Pasta Order Amount is : ₹{pastaAmount}")
      
      # pasta special offer
      if pastaOrder>3:
         self.bruschetta+=1
         print("\n *** Congratulations !! Get 2 Bruschetta free ***  ")
      
      # combo special offer
      if pizzaOrder>3 and pastaOrder>3:
         self.ice_cream+=2
         print("\n *** Congratulations !! Get 2 Chocco Brownies Ice Cream free ***")
         
      print(f"\nYour Total Order is: ₹{total}")
      self.allTotal+=total
      
      return self.allTotal
   
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
menu=Menu()

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
   print(f"""\n====================== Menu ======================
         
 1 Large Pizza = ₹{menu.pizza} 

 2 Large Pizzas = ₹{menu.pizza*2}

 3 Large Pizzas = ₹{menu.pizza*3}

 ***Buy 4 or more Pizzas and get 1.5l of Soft Drink free***
 
--------------------------------

 1 large Pasta = ₹{menu.pasta}

 2 Large Pastas = ₹{menu.pasta*2}

 3 Large Pastas = ₹{menu.pasta*3}

 ***Buy 4 or more Pastas and get 2 Bruschetta free.***

--------------------------------

 ***Buy 4 or more Pizzas and Pastas and get 2 Chocco Brownies Ice Cream free.***
 
--------------------------------\n""")
   
   # customer name
   name=input("Enter your name: ")
   print(f"\nWelcome, {name}\n")

   # customer totol bill
   print(f"\n==>> Your Net Order Amount of the day is : ₹{menu.order()}")
   
   # for more customers
   more=input("\nDo you want to enter from another customer? [y/n] : ")
   
   if more=="Y" or more=="y":
      status=True
   else:
      status=False
      menu.summary()