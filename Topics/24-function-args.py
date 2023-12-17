'''
    Types of Arguments :

    - Positinal argument: int,float,string,variable,list,tuple,dict,etc.
    - Ex. func(8,6,num1,"abc",[5,7,3,10],...)

    - Key-word argument: agrument with key value pair
    - Ex. func(name="abc",age=00,address="xyz")
    
    >> args : myfun(*args) : accepts more than one positional argument in one argument

    >> kwargs : myfun(**kwargs) : accepts keyword argument

'''

# args

def add(*num):
    result=0
    for i in num:
        result+=i
        
    return result

print("Addition:",add(5,10,16,95,32,74,52))

def display(*di):
    for i in di:
        print("Dict:",i)

di1={"name":"Abc"}
di2={"name":"Xyz"}
display(di1,di2)

print()

# kwargs

def info(**data):
    for k,v in data.items():
        print(f"{k}: {v}")

    print("Data:",data)

info(name="Tirth",Age=18,City="Abad")














