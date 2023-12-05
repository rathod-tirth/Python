# nested list

'''
l1=[23,5,[2,55,90,[4],99],92,34,65]

print(l1[2][3][0])
'''


li=[23,45,12,19,23,12,15,10]
num=0

for i in range(len(li)):
    for j in range(i,len(li)):
        if(li[i]==li[j]):
            li.pop(j)
            j+=1

print(li)


'''
# class list

li=[12,3.49,76,"Hello","World",5.51,61,"Good"]

str1=[]
num1=[]
float1=[]

for i in li:
    if(isinstance(i,int)):
        num1.append(i)
    if(isinstance(i,str)):
        str1.append(i)
    if(isinstance(i,float)):
        float1.append(i)

print(str1,num1,float1)


'''





