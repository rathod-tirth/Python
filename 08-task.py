
#task1

for i in range(1,11):
    print(f"{i}) Hello")


#task2

count=0

for i in range(1,11):
    num=int(input("Enter num: "))
    count+=num

print("Total =",count)


#task3

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
