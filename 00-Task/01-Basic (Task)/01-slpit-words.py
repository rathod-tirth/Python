# spliting the string into words and counting no of words

name=input("Enter a Sentence: ")

word=name.split(" ")
count=0

for element in word:
    count+=1

print(f"No. of words: {count}")
