class  Student:
   name="A"
   contact="6656"

   def setName(self,name):
      self.name=name
   
   def getName(self):
      return self.name
   
   def setContanct(self,contact):
      self.contact=contact
   
   def getContact(self):
      return self.contact

s= Student()

s.setContanct("BCA121")
print(s.getContact())