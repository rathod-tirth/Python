# Area finder for circle, triangle, Rectangle

status=True

while(status):
   print("""\n============ Area Finder ============
         
               1. Circle
               2. Triangle
               3. Rectangle\n\n""")

   choice=int(input("Enter choice: "))
   result=0

   print()

   if choice<4:
      if choice==1:
         radius=int(input("Enter Radius: "))
         result=3.141*radius**2
         print(f"Area of the Circle: {result}\n")
      elif choice==2:
         base=int(input("Enter Base: "))
         height=int(input("Enter Height: "))
         result=base*height/2
         print(f"Area of the Triangle: {result}\n")
      elif choice==3:
         length=int(input("Enter Length: "))
         width=int(input("Enter Width: "))
         result= length*width
         print(f"Area of Rectangle: {result}\n")
   else:
      print("Wrong Choice!! Pls Enter Again!!")
      continue
   
   more=input("Do you want to continue? [y/n]: ")
   
   if more=="Y" or more=="y":
      status=True
   else:
      status=False
      print("\nThank You")