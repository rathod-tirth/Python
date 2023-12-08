# ascending order

li=[21,56,47,8,23,42,10,46,68,92,37]

for i in range(len(li)):
    for j in range(i,len(li)):
        if(li[i]>li[j]):
            li[i],li[j]=li[j],li[i]
print(li)
        
        
# descending order

for i in range(len(li)):
    for j in range(i,len(li)):
        if(li[i]<li[j]):
            li[i],li[j]=li[j],li[i]
print(li)
