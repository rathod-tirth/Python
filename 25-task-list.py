# list task


# remove duplication

li=[23,45,12,19,23,12,15,10,45,65,19,23,15,12]
newLi=[]

for i in li:
    if(i not in newLi):
        newLi.append(i)

print("Original List",li)
print("New List:",newLi)

print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

# sorting list based on there class

li2=[12,3.49,76,"Hello","World",5.51,61,"Good"]

str1=[]
num1=[]
float1=[]

for i in li2:
    if(isinstance(i,int)):
        num1.append(i)
    if(isinstance(i,str)):
        str1.append(i)
    if(isinstance(i,float)):
        float1.append(i)

print("Original List",li2)
print(f"String = {str1} \nNum = {num1} \nFloat = {float1}")

