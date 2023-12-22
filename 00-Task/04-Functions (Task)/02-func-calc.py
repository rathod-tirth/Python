# Function-Calculator

def calc(a,b,choice):
    result=0
    if(choice==1):
        result=a+b
    elif(choice==2):
        result=a-b
    elif(choice==3):
        result=a*b
    elif(choice==4):
        if not(b==0):
            result=a/b
        else:
            print("Error")
    elif(choice==5):
        if not(b==0):
            result=a%b
        else:
            print("Error")

    return result

status=True

while(status):

    print("""===========Choice Board===========

            1. Addition
            2. Substraction
            3. Multiplication
            4. Division
            5. Modulo
            6. Exit""")

    choice=int(input("\nEnter choice: "))

    if(choice<6):
        num1=int(input("\nEnter first num: "))
        num2=int(input("Enter second num: "))

        result=calc(num1,num2,choice)

        print("Result:",result)
    else:
        print("Exited")
        status=False
        break

    more=input("Do you want to continue? [y/n]: ")

    if not(more=="Y" or more=="y"):
        status=False
        print("Thank you for using the calculator")
















