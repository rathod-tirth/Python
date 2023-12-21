# task

class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def identical(self,obj):
        if(self.a==obj.a and self.b==obj.b):
            return "All the values are identical"
        else:
            return "Values are not identical"
        

a1=A(12,5)
a2=A(12,5)

print(a1.identical(a2))
