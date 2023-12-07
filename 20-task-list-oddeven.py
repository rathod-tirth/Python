# odd even list

li=[21,56,47,8,23,42,10,46,68,92,37]

odd=0
even=0

for element in li:
    if(element%2==0):
        even+=1
    else:
        odd+=1

print(f"Odd: {odd} Even: {even}")
