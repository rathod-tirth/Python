# no. of repeated  words

name=input("Enter : ")
char=input("Enter char:")

count=0

if char in name:
    for element in name:
        if(char == element):
            count+=1
    print(f"No. of words: {count}")
else:
    print("Character doesn't exist")
