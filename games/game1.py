import random
#generate a random number between 1 and 3
#rock paper scissors
#please enter your choice (rock, paper, scissors) rock
#computer choice is rock ["rock", "paper", "scissors"]
#tie
#please enter your choice (rock, paper, scissors) paper
#computer choice is scissors
#you lose game over score is  -0
# no  = random.randint(0,2)
# print(no)

print("WELCOME TO ROCK PAPER SCISSORS GAME")

choices = ["rock", "paper", "scissors"]
userChoice =""
score = 0
while True:
    print("please enter your choice (rock, paper, scissors)")
    userChoice = input()
    print("computer Turn Computer choice is ",end="")
    computerChoice = choices[random.randint(0,2)]
    print(computerChoice)
    if userChoice == computerChoice:
        print("Tie")
    elif (userChoice == "rock" and computerChoice == "scissors") or (userChoice == "paper" and computerChoice == "rock") or (userChoice == "scissors" and computerChoice == "paper"):
        print("You win")    
        score += 1
    else:
        print("You lose game over score is", score)
        break
    