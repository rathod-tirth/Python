# guess the lucky num

'''
    - here list of number is shuffled and given to user and computer
    - from the original list a lucky number is picked
    - user and computer tries to guess the number from the own respective lists
    - if one them guess it correctly the number gets removed from there and original list
    - repeating this process until one of them have an empty list
    - One with an empty list is declared as the winner
'''

import random

li=[14,26,85,94,73,37]

random.shuffle(li)

c_li=li[:3]
u_li=li[3:]

c_score=0
u_score=0

while (c_li and u_li):
    lucky=random.choice(li)
    print("=====================================")
    print("Original List:",li)
    print()
    
    print("User List:",u_li)
    u_lucky=int(input("Guess the num: "))

    while (u_lucky not in u_li):
        print("\nPlease Guess the number from the list")
        u_lucky=int(input("Guess the num: "))

    print("You Guessed:",u_lucky)
    print()

    c_lucky=random.choice(c_li)
    print("Computer List:",c_li)
    print("Computer Guessed:",c_lucky)
    print()

    print("========================")
    print("User Number:",u_lucky)
    print("Computer Number:",c_lucky)
    print("Lucky Number:",lucky)
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






        
