# guess the lucky num

'''
    - here list of number is shuffled and given to user and computer
    - from the original list a lucky number is picked
    - user and computer tries to guess the number from the own respective lists
    - if one them guess it correctly the number gets removed from there and original list
    - repeating this process until one of them have an empty list
    - Whoever has an empty list is declared as the winner

    Note: all the guessing process by the user is also done automated
'''

import random

li=[14,26,85,94,73,37,41,55,3,60]

random.shuffle(li)

c_li=li[:5]
u_li=li[5:]

print("Original List:",li)
print("Computer List:",c_li)
print("User List:",u_li)
print()

c_score=0
u_score=0

while (c_li and u_li):
    lucky=random.choice(li)
    c_lucky=random.choice(c_li)
    u_lucky=random.choice(u_li)

    print("Lucky Number:",lucky)
    print("Computer Number:",c_lucky)
    print("User Number:",u_lucky)
    print("========================")

    if(c_lucky==lucky):
        li.remove(lucky)
        c_li.remove(lucky)
        c_score+=1
        print("Computer Wins")
    elif(u_lucky==lucky):
        li.remove(lucky)
        u_li.remove(lucky)
        u_score+=1
        print("User Wins")
    else:
        print("Draw")

    print(f"Computer: {c_score} | User: {u_score}")
    print("========================\n\n")






        
