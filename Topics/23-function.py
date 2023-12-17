'''
    Function : A block of code which can be used again

    >> Functions are declared with def keyword

    >> syntax :
    
        def fun_name():
            code...

    >> Types of Function :

    1. User Defined Function:
        1. o/o
        2. w/o
        3. o/w
        4. w/w
        
    2. In-built Function:
        1. print()
        2. type()
        3. len()
        ...

'''
# defination

# declaration
def welcome():
    print("Welcome, thank you for coming")

# calling
welcome()

# parameter and return value

def add(num1,num2):
    return num1+num2

print("Addition:",add(15,4))

# global variable

def info():
    global name
    name=input("Enter your name: ")
    print("Name:",name)

info()
print("New Member:",name)






















