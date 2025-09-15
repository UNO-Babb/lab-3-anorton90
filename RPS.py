#RPS.py
#Name:Alyssia Norton
#Date:9-15
#Assignment:lab 3
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  playAgain = "Y"
  while playAgain == "Y":
    #Create a loop that continues as long as the user wants to play.
    #User can play as many games as they wish.
    computer = random.choice (["R", "P", "S"])
    player = input ("Choose your weapon (R, P, S):")


    #Randomly choose the computer between 'R', 'P', or 'S'
    #Prompt the user for their RPS selection
    #Determine winner and state what happened to the user

    if computer == "R":
      print ("computer chose Rock")
    elif computer == "P":
      print ("computer chose Paper")
    else:    
      print ("computer chose scissors")

    if player == "R":
      print ("player chose Rock")
    elif player == "P":
      print ("player chose Paper")
    else:    
      print ("player chose scissors")

    if player == "R" and computer == "R":
      print ("Tie")
      ties = ties + 1
    if player == "R" and computer == "P":
      print ("Computer wins")
      losses = losses + 1
    if player == "R" and computer == "S":
      print ("You win!")
      wins = wins + 1
    
    if player == "S" and computer == "S":
      print ("Tie")
      ties = ties + 1
    if player == "S" and computer == "R":
      print ("Computer wins")
      losses = losses + 1
    if player == "S" and computer == "P":
      print ("You win!")
      wins = wins + 1
    
    if player == "P" and computer == "P":
      print ("Tie")
      ties = ties + 1
    if player == "P" and computer == "S":
      print ("Computer wins")
      losses = losses + 1
    if player == "P" and computer == "R":
      print ("You win!")
      wins = wins + 1
        

    #Ask the user if they would like to play again.
    playAgain = input("Play Again? (Y/N)")

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
