# Guess the Lucky number task

import random

status=True

while(status):
    lucky_num=random.randint(1,100)

    print(lucky_num)

    user_num=int(input("Guess the num: "))

    for chance in range(1,5):
        if(lucky_num>user_num):
            print("hint: think larger num")
            user_num=int(input("Guess the num: "))
        elif(lucky_num<user_num):
            print("hint: think smaller num")
            user_num=int(input("Guess the num: "))
        elif(lucky_num==user_num):
            print("You Guessed the num")
            break

    new=input("New Game?? [y/n]")
    if(new=="Y" or new=="y"):
        status=True
    else:
        status=False
