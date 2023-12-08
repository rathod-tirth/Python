# loop pattern task

# task 1
'''
num=int(input("Enter num: "))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
'''

# task2
'''
for x in range(5):
    for i in range(5):
        if(x==2 and i==2):
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()
'''

'''
for x in range(5):
    for i in range(5):
        if(x==i):
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()
'''

'''
for x in range(5):
    for i in range(5):
        if(x>=i):
            print("*",end=" ")
    print()
'''

'''
for x in range(1,6):
    for i in range(1,x+1):
        if(i%2==0):
            print(0,end=" ")
        else:
            print(1, end=" ")
    print()
'''

'''
for x in range(1,6):
    for i in range(1,x+1):
        print(i,end=" ")
    print()
'''

'''
count=0

for x in range(5):
    for i in range(0,x):
        count+=1
        print(count,end=" ")
    print()
'''

'''
alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
count=-1

for i in range(1,6):
    for j in range(1,i+1):
        count+=1
        print(alpha[count],end=" ")
    print()
'''

'''
alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for i in range(5):
    for j in range(0,i+1):
        print(alpha[j],end=" ")
    print()
'''

'''
for i in range(1,6):
    print(" "*(5-i)*2+"* "*i)
'''

'''
for i in range(1,6):
    print("* "*(6-i)+" "*i)
'''

'''
for i in range(1,6):
    print(" "*(5-i)+"* "*i)
'''

'''
for i in range(1,6):
    print(" "*(i)+"* "*(6-i))
'''


























