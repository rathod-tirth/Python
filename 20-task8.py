# lucky num

import random

li=[14,26,85,94,73,13,47,2,53,64,45,79]

c_li=li[0:6]
u_li=li[6:12]

c_score=0
u_score=0

while(c_li and u_li):
    lucky=random.choice(li)

    if(lucky in c_li):
        c_li.remove(lucky)
        li.remove(lucky)
        c_score+=1
        print("Computer win",c_li)
    elif(lucky in u_li):
        u_li.remove(lucky)
        li.remove(lucky)
        u_score+=1
        print("User win",u_li)

    print("Computer score:",c_score)
    print("User score:",u_score)
    print("========================")

    if(c_li==[] or u_li==[]):
        
        break
