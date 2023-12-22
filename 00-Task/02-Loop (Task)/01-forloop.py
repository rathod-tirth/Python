# loop task

# task1 : 

'''
    1) Hello
    2) Hello
    3) Hello...
'''

for i in range(1,11):
    print(f"{i}) Hello")


# task2: Summation

count=0

for i in range(1,11):
    num=int(input("Enter num: "))
    count+=num

print("Total =",count)


#task3: odd even

even=0
odd=0

for i in range(1,11):
    num=int(input("Enter num: "))
    if num%2==0:
        even+=1
    else:
        odd+=1

print("no. of Even =",even)
print("no. of Odd =",odd)
