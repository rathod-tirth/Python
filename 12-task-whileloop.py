# Guess the Lucky number task

import random

status=True

while(status):
    lucky_num=random.randint(1,100)

    print(lucky_num)

    for chance in range(1,6):
        user_num=int(input("Guess the num: "))
        
        if(lucky_num>user_num and chance<5):
            print("hint: think larger num")
        elif(lucky_num<user_num and chance<5):
            print("hint: think smaller num")
        elif(lucky_num!=user_num and chance==5):
            print("Game Over")
        elif(lucky_num==user_num):
            print("You Guessed the num")
            break

    new=input("New Game?? [y/n]: ")
    if(new=="Y" or new=="y"):
        status=True
    else:
        status=False
