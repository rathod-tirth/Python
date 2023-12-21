class Product:
   mobile=5000
   __laptop=20000

   def display(self):
      print(self.mobile)
      print(self.__laptop)
   
   def update(self,laptop):
      self.__laptop=laptop

product=Product()
product.display()

product.mobile=10000
product.update(50000)

product.display()