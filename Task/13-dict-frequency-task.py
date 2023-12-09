# frequency task: counts how many time the word is repeated in a dict format

text=input("Enter a sentence: ")

li=text.split(" ")

print(li)

obj={}
count=0

for i in li:
    count=li.count(i)
    obj[i]=count

print(obj)
