# nested loop

for i in range(5):
    print("* "*5)

print(">>>>>>>> nested pattern")
for i in range(5):
    for j in range(5):
        print("* ", end="")
    print()


print(">>>>>>>> pyramid")
for i in range(1,6):
    print("* "*i)

print(">>>>>>>> nested pyramid")
for i in range(5):
    for j in range(5):
        if(i>=j):
            print("* ", end="")
    print()

print(">>>>>>>> pyramid")
for i in range(1,6):
    print(" "*(5-i)+"*"*i)

print(">>>>>>>> nested pyramid")
for i in range(1,6):
    for j in range(6,i+1,-1):
        print(" ",end="")
    print("*"*i,end="")
    print()


