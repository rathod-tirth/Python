# counting how many times does a character reapeats

name=input("Enter Sentence: ")
char=input("Enter Character: ")

count=0

if char in name:
    for element in name:
        if(char == element):
            count+=1
    print(f"No. of Character {char}: {count}")
else:
    print("Character doesn't exist")
