# Jumping statements in python

'''

break : will stop loop
pass : when block of code syntatically needed but no need to create any logic
continue : will skip the iteration

'''

for i in range(5):
    if(i==3):
        break
    if(i==1):
        pass
    if(i==2):
        continue
    print("Hello")
