import tkinter as tk
import random

root = tk.Tk() # main screen
root.geometry("500x500") # screen resolution
root.title("Mini Game") # window title

heading= tk.Label(root, text="Mini Game", font=("courier", 24,"bold"), pady=25) # heading
heading.pack()

li=["ROCK","PAPER","SCISSOR"]

# variables
userChoice=tk.StringVar()
compChoice=tk.StringVar()
resultText=tk.StringVar()
userScore=tk.IntVar()
compScore=tk.IntVar()

# initial values
userChoice.set("--")
compChoice.set("--")
resultText.set("--")
userScore.set(0)
compScore.set(0)

# result function
def handleChoice(val):
   userChoice.set(val)
   compChoice.set(random.choice(li))

   if userChoice.get() == li[0] and compChoice.get() == li[2] or userChoice.get() == li[1] and compChoice.get() == li[0] or userChoice.get() == li[2] and compChoice.get() == li[1]:
      resultText.set("You Win!!")
      userScore.set(userScore.get()+1)
   elif userChoice.get()==compChoice.get():
      resultText.set("Draw!!")
   else:
      resultText.set("Computer Win!!")
      compScore.set(compScore.get()+1)

   text = tk.Label(root, textvariable=resultText, font=("sans", 18, "bold"))
   text.place(x=30, y=300)

# buttons
btn=tk.Button(root, text="ROCK",font=("arial",18,"bold"), bg="lightgray", relief="solid", height=2, width=8, command=lambda:handleChoice(li[0]))
btn.place(x=30,y=100)
btn=tk.Button(root, text="PAPER",font=("arial",18,"bold"), bg="lightgray", relief="solid", height=2, width=8, command=lambda:handleChoice(li[1]))
btn.place(x=180,y=100)
btn=tk.Button(root, text="SCISSOR",font=("arial",18,"bold"), bg="lightgray", relief="solid", height=2, width=8, command=lambda:handleChoice(li[2]))
btn.place(x=330,y=100)

# user choice board
text= tk.Label(root, text="Your Turn: ", font=("sans", 16))
text.place(x=30,y=200)

userChoiceText= tk.Label(root, textvariable=userChoice, font=("sans", 16, "bold"))
userChoiceText.place(x=140,y=200)

# computer choice board
text= tk.Label(root, text="Computer's Turn: ", font=("sans", 16))
text.place(x=30,y=250)

compChoiceText= tk.Label(root, textvariable=compChoice, font=("sans", 16, "bold"))
compChoiceText.place(x=200,y=250)

# user score board
text= tk.Label(root, text="Y: ", font=("sans", 16))
text.place(x=350,y=200)

userScoreText=tk.Label(root, textvariable=userScore, font=("sans", 20, "bold"))
userScoreText.place(x=380,y=195)

# computer score board
text= tk.Label(root, text="C: ", font=("sans", 16))
text.place(x=350,y=250)

userScoreText=tk.Label(root, textvariable=compScore, font=("sans", 20, "bold"))
userScoreText.place(x=380,y=245)

root.mainloop() # to run the program