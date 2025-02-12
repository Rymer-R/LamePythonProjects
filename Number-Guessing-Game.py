#1st python project
#A Number Guessing game in python
import random
  
#------start------
#1. Ask the user a range
while True:
  try:
    lower_range = int(input("Enter a lower range: "))
    higher_range = int(input('Enter a higher range: '))
    if lower_range >= higher_range:
      print("Higher range must be greater than lower range. Please try again!")
      continue
  except:
    print("Invalid value(s), please enter a number...")
    continue
  
  #3. Generate random number between that range
  
  random_number = random.randrange(lower_range, higher_range)
  
  #4. Prompt the user to guess
  #4.1 Add a counter
  count = 0
  
  while True:
    try:
      guessed_number = int(input("Guess the number: "))
    except:
      print("Please enter a numeric value!")
      continue
  
    count+=1
  
  #5. if the guess is greater than the generated number print "too high!"
    
    if guessed_number > random_number:
      print(f"Too high!\nGuesses: {count}")
      
  #6. if the guess is lower than the generated number print "too low"
    
    elif guessed_number < random_number:
      print(f"Too low!\nGuesses: {count}")
      
  #7. if the guess is equal then print "current guess"
    
    else:
      print(f"Correct!!, You took {count} attempts")
      break

  #8 Play again moment
  
  play_again = input("Do you want to play again? (y/n): ").strip().lower()
  if play_again == "n" or play_again == "no":
    break
  elif play_again not in ("y", "yes"):
    break  
