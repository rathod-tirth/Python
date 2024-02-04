# Mini IPL game

import random

class GameData:
   def __init__(self):
      self.team=["CSK","MI","GT","RCB","SRH","KKR"]
      self.user_team=""
      self.comp_team=""
      
class GameRandom:
   def tossGenration(self):
      result=random.randint(0,1)
      return result

class GameLogic(GameData,GameRandom):
   def teamSelection(self):
      user_choice=int(input("\nEnter your choice : "))
      
      # for out of bound team selection
      while user_choice>len(self.team) or user_choice<1:
         print("\nWrong Input Pls enter again")
         user_choice=int(input("Enter your choice : "))

      self.user_team=self.team[user_choice-1]
      self.team.remove(self.user_team)
      self.comp_team=random.choice(self.team)
      
   def toss(self):
      user_toss=int(input("Enter your choice : "))
      
      while user_toss>1:
         print("\nWrong Input Pls enter again")
         user_toss=int(input("Enter your choice : "))

      result=self.tossGenration()

class PrintOut(GameLogic):
   def __init__(self):
      super().__init__()
      print("Team Selection".center(50)+f"\n{dash}\n")
      print("Choose Your Team : \n")
      
      # printing out the teams
      count=1
      for i in self.team:
         print(f"Press {count} for : {i}")
         count+=1
         
   def teamPrint(self):
      self.teamSelection()
      
      print("\nYour Team :",self.user_team)
      print("Opponent's Team :",self.comp_team)
      print(f"\n{self.user_team} vs {self.comp_team}")
      
   def tossPrint(self):
      print("Toss".center(50)+f"\n{dash}\n")
      print("Chose your Toss : \n")
      print("Press 1 for : Head\nPress 2 for : Tail\n")
   
# title
dash="----------------------------------------------------"
print("IPL".center(50)+f"\n{dash}")

ipl=PrintOut()
ipl.teamPrint()
ipl.tossPrint()