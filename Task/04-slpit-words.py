# split string into words

name=input("Enter : ")

word=name.split(" ")
count=0

for element in word:
    count+=1

print(f"No. of words: {count}")
