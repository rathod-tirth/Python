# hybrid inheritance

class A:
    print("Hello A")
    def var(self):
        num1=int(input("Enter num1: "))
        num2=int(input("Enter num2: "))

class B(A):
    print("Hello B")
    
    def add(self):
        result=self.num1+self.num2
        return result

class C(A):
    print("Hello C")

    def multi(self):
        result=self.num1*self.num
        return result

class D(B,C):
    print("Hello D")
    #result=num1+num2
    #print("Result:",result)

obj=D()
