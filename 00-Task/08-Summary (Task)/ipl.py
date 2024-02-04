# ipl cricket match mini game using all the core and advance concept of python

import random

# title
dash="----------------------------------------------------"
print("IPL".center(50)+f"\n{dash}")

# available teams
print("Team Selection".center(50)+f"\n{dash}\n")
print("Choose Your Team : \n")
team=["CSK","MI","GT","RCB","SRH","KKR"]

# printing out the teams
count=1
for i in team:
   print(f"Press {count} for : {i}")
   count+=1

# user team selection
user_choice=int(input("\nEnter your choice : "))

# for out of bound team selection
while user_choice>len(team):
   print("\nWrong Input Pls enter again")
   user_choice=int(input("Enter your choice : "))
   
user_team=team[user_choice-1]
print("\nYour Team :",user_team)
team.remove(user_team)

# computer team selection
comp_team=random.choice(team)
print("Opponent's Team :",comp_team)

print(f"\n{user_team} vs {comp_team}")

# toss
toss=["Head","Tail"]

print("Toss".center(50)+f"\n{dash}\n")
print("Chose your Toss : \n")
print("Press 1 for : Head\nPress 2 for : Tail\n")

user_toss=int(input("Enter your choice : "))
while user_toss>len(toss):
   print("\nWrong Input Pls enter again")
   user_toss=int(input("Enter your choice : "))

toss_result=random.choice(toss)
print("\nToss :",toss_result)

batball=["Bat","Ball"]
user_batball=""
comp_batball=""

if toss[user_toss-1]==toss_result:
   print("You win the toss\n")
   print("Press 1 for : Bat\nPress 2 for : Ball\n")
   
   user_batball=int(input("Enter your choice : "))
   while user_batball>len(batball):
      print("\nWrong Input Pls enter again")
      user_batball=int(input("Enter your choice : "))

   print(f"\n{user_team} choose to {batball[user_batball-1]}")
else:
   print("Computer win the toss\n")
   comp_batball=random.choice(batball)
   print(f"{comp_team} choose to {comp_batball}")

possible_score=[0,1,2,3,4,6,"wide","no ball","wicket"]
runs=0
wicket=0
ball=0

if user_batball.casefold()=="bat":
   scoreboard=f"{user_team} : {runs}/{wicket} (0.{ball})"
   
   for i in range(6):
      print(scoreboard)
      score=random.choice(possible_score)
      
      if score==0:
         ball+=1
         print(scoreboard)
      elif score==1:
         ball+=1
         runs+=1
         print(scoreboard)
      elif score==2:
         ball+=1
         runs+=2
         print(scoreboard)
      elif score==3:
         ball+=1
         runs+=3
         print(scoreboard)
      elif score==4:
         ball+=1
         runs+=4
         print(scoreboard)
      elif score==6:
         ball+=1
         runs+=6
         print(scoreboard)
      elif score=="wide":
         i-=1
         runs+=1
         print(scoreboard)
      elif score=="no ball":
         i-=1
         runs+=1
         print(scoreboard)
      elif score=="wicket":
         ball+=1
         wicket+=1
         print(scoreboard)
         break
      
else:
   score=f"{comp_team} : {runs}/{wicket} (0.{ball})"

