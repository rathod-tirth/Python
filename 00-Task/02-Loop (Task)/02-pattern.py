# loop pattern task

# task 1: user table
'''
num=int(input("Enter num: "))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
'''

# task2:

'''
    * * * * * 
    * * * * * 
    * * $ * * 
    * * * * * 
    * * * * *
'''

'''
for x in range(5):
    for i in range(5):
        if(x==2 and i==2):
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()
'''

# task3:

'''
    $ * * * * 
    * $ * * * 
    * * $ * * 
    * * * $ * 
    * * * * $ 
'''

'''
for x in range(5):
    for i in range(5):
        if(x==i):
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()
'''

# task4:

'''
    * 
    * * 
    * * * 
    * * * * 
    * * * * *
'''

'''
for x in range(5):
    for i in range(5):
        if(x>=i):
            print("*",end=" ")
    print()
'''

# task5:

'''
    1 
    1 0 
    1 0 1 
    1 0 1 0 
    1 0 1 0 1 
'''

'''
for x in range(1,6):
    for i in range(1,x+1):
        if(i%2==0):
            print(0,end=" ")
        else:
            print(1, end=" ")
    print()
'''

# task6:

'''
    1 
    1 2 
    1 2 3 
    1 2 3 4 
    1 2 3 4 5 
'''

'''
for x in range(1,6):
    for i in range(1,x+1):
        print(i,end=" ")
    print()
'''

# task7:

'''
    1 
    2 3 
    4 5 6 
    7 8 9 10 
'''

'''
count=0

for x in range(5):
    for i in range(0,x):
        count+=1
        print(count,end=" ")
    print()
'''

# task8:

'''
    A 
    B C 
    D E F 
    G H I J 
    K L M N O 
'''

'''
count=0

for i in range(5):
    for j in range(0,i+1):
        print(chr(65+count),end=" ")
        count+=1
    print()
'''

# task9:

'''
    A 
    A B 
    A B C 
    A B C D 
    A B C D E
'''

'''
for i in range(5):
    for j in range(0,i+1):
        print(chr(65+j),end=" ")
    print()
'''

# task10:

'''
        * 
      * * 
    * * * 
  * * * * 
* * * * *
'''

'''
for i in range(1,6):
    print(" "*(5-i)*2+"* "*i)

# task11:
'''

'''
    * * * * *  
    * * * *   
    * * *    
    * *     
    *
'''

'''
for i in range(1,6):
    print("* "*(6-i)+" "*i)
'''

# task12:

'''
    * 
   * * 
  * * * 
 * * * * 
* * * * *
'''

'''
for i in range(1,6):
    print(" "*(5-i)+"* "*i)
'''

# task13:

'''
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
'''

'''
for i in range(1,6):
    print(" "*(i)+"* "*(6-i))
'''


























