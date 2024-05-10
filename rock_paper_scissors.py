import random
user = int(input('Enter your choice : '))
# 0 for Rock          # Rules 1. Rock > Paper, Paper wins
# 1 for Paper                 2. Paper > Scissors, Scissors win
# 2 for Scissors              3. Scissors > Rock, Rock wins
if user >=3 or user < 0 :
    print ('Please enter a valid choice!!!!!!!!!!')
else:
    computer = (random.randint(0,2))
    print ("Computer's choice : ", computer)
    if user == computer:
        print ("It's a tie!!!!! Try again")
    elif user == 0 and computer == 1:
        print ("You lose")
    elif user == 1 and computer == 0:
        print ("You win")
    elif user == 1 and computer == 2:
        print ("You lose")
    elif user == 2 and computer == 1:
        print ("You Win")
    elif user == 0 and computer == 2:
        print ("You Win")
    elif user == 2 and computer == 0:
        print ("You lose")

    
