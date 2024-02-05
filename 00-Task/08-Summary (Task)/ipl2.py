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
      self.batteam=""
      self.ballteam=""
      
      self.score=[0,1,2,3,4,6,'W','NB','WIDE']
      self.runs=0
      self.innings=1
      
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
         
         while user_batORball>2 or user_batORball<1:
            print("\nWrong Input Pls enter again")
            user_batORball=int(input("Enter your choice : "))

      else:
         result=random.choice(self.batORball)
      
      if result.lower()=='bat':
         self.batteam=self.user_team if self.tosswinner==self.user_team else self.comp_team
         self.ballteam=self.comp_team if self.tosswinner==self.user_team else self.user_team
      else:
         self.batteam=self.comp_team if self.tosswinner==self.user_team else self.user_team
         self.ballteam=self.user_team if self.tosswinner==self.user_team else self.comp_team
      return result
   
   def scoreLogic(self):
      runs=0
      wicket=0
      ball=0
      printball=0
      scoreboard=""
      freehit=False
      
      while ball<6:
         ball+=1
         
         # score
         current_score=random.choice(self.score)
         scoreboard+=f"{current_score} "
         
         if current_score=="W" and not freehit:
            wicket=1
         elif current_score in ["WIDE","NB"]:
            ball-=1
            runs+=1
         elif isinstance(current_score,int):
            runs+=current_score
            
         # ball
         if ball%6==0:
           printball=ball/6
         else: 
            printball=ball/10
         
         if self.innings==1:
            print(f"\n{self.user_team} VS {self.comp_team} | {self.batteam} : {runs}/{wicket} ({printball}) | {scoreboard}")
         else:
            req_runs=self.runs-runs if self.runs-runs>0 else 0
            print(f"\n{self.user_team} VS {self.comp_team} | {self.batteam} : {runs}/{wicket} ({printball}) | {req_runs} runs in {6-ball} balls | {scoreboard}")

            if runs>=self.runs:
               break
         
         if current_score=="W" and not freehit:
            break
         if current_score=="NB":
            freehit=True
         else:
            freehit=False
            
         input("Press Enter to Continue...")
      
      if self.innings==1:
         self.runs=runs+1
         print(f"\n{self.ballteam} needs {self.runs} runs to win")
         
         self.innings=2
         self.batteam,self.ballteam=self.ballteam,self.batteam
         input("Press Enter to Continue...")
         self.scoreLogic()
      else:
         if runs>=self.runs:
            print(f"\n{self.batteam} won the match by 1 wicket")
         else:
            print(f"\n{self.ballteam} won the match by {self.runs-runs} runs")

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
      
   def scorePrint(self):
      self.scoreLogic()
         
      
# title
dash="----------------------------------------------------"
print("IPL".center(50)+f"\n{dash}")

while True:
   ipl=PrintOut()
   ipl.teamPrint()
   ipl.tossPrint()
   ipl.batORballPrint()
   ipl.scorePrint()
   
   more=input("\nDo you want to continue? [y/n] : ")
   
   if more.lower()!='y':
      print("\nThank you for playing")
      break