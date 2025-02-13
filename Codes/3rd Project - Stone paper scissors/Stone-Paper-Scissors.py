#3rd Project for Lame python projects
#Stone paper scissors (simple one actually unless we're adding score and replay system T-T)

import random

#1. show the rules to the user
print('''Rules:
Stone vs Paper : Paper wins
Paper vs Scissors : Scissors wins
Scissors vs Stone : Stone wins
1 - stone
2 - paper
3 - scissors
First to five wins!''')
#1.1 setup tuple/rules
rules = ("stone", "paper", "scissors")
#1.2 add a score counter to make it more fun, first to five wins
user_score = 0
computer_score = 0
while True:
    #1.3 let the computer choose
    computer = random.choice(rules)
    #2. ask for input from the user or make the user select between stone, paper and scissors
    try:
        chosen = int(input("Choose your option: ")) - 1
        if chosen < 0:
            print("Please choose a valid option")
            continue
        option = rules[chosen]
    except:
        print("Please choose a valid option")
        continue
    else:
        #3. if equal then draw
        if option == computer:
            print("draw!!, Nobody gets the point")
        #4. if one of the conditions favoured for the winning of user are satisfied user wins
        elif (computer == "stone" and option == "paper") or \
                (computer == "paper" and option == "scissors") or \
                (computer == "scissors" and option == "stone"):
            print("You won!!")
            user_score +=1
        #5. else computer wins
        else:
            print("You lost!, Computer wins!!")
            computer_score += 1
        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")
        #6. ask for playing again
        if computer_score == 5 or user_score == 5:
            if computer_score == 5:
                print("Computer won with the score of 5")
            else:
                print("You won with the score of 5")
            while True:
                play_again = input("Do you want to play again? (y/n): ").lower()
                if play_again in ("no", "n"):
                    print("Thanks, see you next time! :D")
                    exit()
                elif play_again in ("yes", "y"):
                    print("---Lets play again---")
                    computer_score = 0
                    user_score = 0
                    break
                else:
                    print("Invalid response...")
