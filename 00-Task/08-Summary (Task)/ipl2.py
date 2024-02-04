# Mini IPL game

import random

class GameData:
   def __init__(self):
      # team
      self.team=["CSK","MI","GT","RCB","SRH","KKR"]
      self.user_team=""
      self.comp_team=""
      
      # toss
      self.coin=["Head","Tail"]
      self.tossresult=-1
      self.tosswinner=""
      
      self.batORball=["Bat","Ball"]
      self.bat=""
      
      self.score=[0,1,2,3,4,6,'W','NB','WIDE']
      
class GameRandom:
   pass

class GameLogic(GameData,GameRandom):
   def teamSelection(self):
      # user team choice
      user_choice=int(input("\nEnter your choice : "))
      
      # for out of bound team selection
      while user_choice>len(self.team) or user_choice<1:
         print("\nWrong Input Pls enter again")
         user_choice=int(input("Enter your choice : "))

      # assiging user and comp team
      self.user_team=self.team[user_choice-1]
      self.team.remove(self.user_team)
      self.comp_team=random.choice(self.team)
      
   def tossLogic(self):
      # user toss choice
      user_toss=int(input("Enter your choice : "))
      
      while user_toss>len(self.coin) or user_toss<1:
         print("\nWrong Input Pls enter again")
         user_toss=int(input("Enter your choice : "))

      self.tossresult=random.choice(self.coin)
      
      if self.tossresult==self.coin[user_toss-1]:
         self.tosswinner=self.user_team
      else:
         self.tosswinner=self.comp_team
   
   def batORballLogic(self):
      if self.tosswinner==self.user_team:
         user_batORball=int(input("Enter your choice : "))
         result=self.batORball[user_batORball-1]
         
         while user_batORball>len(self.batORball):
            print("\nWrong Input Pls enter again")
            user_batORball=int(input("Enter your choice : "))
         
      else:
         comp_batORball=random.choice(self.batORball)
         result=comp_batORball

      if result.lower()=='bat':
         self.bat=self.tosswinner
      elif self.tosswinner==self.user_team:
         self.bat=self.comp_team
      else:
         self.bat=self.user_team
         
      return result
      
   
   def scoreLogic(self):
      pass
      # f"{user_team} : {runs}/{wicket} (0.{ball})"
         

class PrintOut(GameLogic):
   # initial render
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
      self.tossLogic()
      
      print("\nToss :",self.tossresult)
      print(f"{self.tosswinner} win the toss\n")
   
   def batORballPrint(self):
      if self.tosswinner==self.user_team:
         print("Press 1 for : Bat\nPress 2 for : Ball\n")
      
      result=self.batORballLogic()
      print(f"\n{self.tosswinner} choose to {result}")
      
      # if result.lower()=="bat":
      #    self.bat=self.tosswinner
      # else:
         
      
# title
dash="----------------------------------------------------"
print("IPL".center(50)+f"\n{dash}")

ipl=PrintOut()
ipl.teamPrint()
ipl.tossPrint()
ipl.batORballPrint()