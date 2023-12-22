'''

    >> Anonymous Function In Python : A Function without Name

    >> Lambda Function : It is an anonymous function in python

    - It can take many arguments but can only return single expression

    Syntax :

    >> lambda parameters : return

    >> lambda functions is widely used for mathemetical operations

'''

add=lambda x,y: x+y

print("Addition:",add(5,10))

string=lambda x:x

print("String:",string("Hello"))

# function returns lambda function

def add(x):
    return lambda y:x+y

sums=add(5)

print("Addition:",sums(10))

