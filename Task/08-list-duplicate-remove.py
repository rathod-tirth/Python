
# removes duplicate numbers from the list

li=[23,45,12,19,23,12,15,10,45,65,19,23,15,12]
newLi=[]

for i in li:
    if(i not in newLi):
        newLi.append(i)

print("Original List",li)
print("New List:",newLi)



