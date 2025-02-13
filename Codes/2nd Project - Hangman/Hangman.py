#2nd Project for Lame Python Projects
#Hangman without Hanged man 
#----start----
import random

'''1. Have to create a list of words or maybe use dictionary for categories but dunno how to work with dictionary
will use txt file then for storing a billion words :P'''

with open("words.txt", "r") as file:
  words = file.read().splitlines()

#2. Use random to select a word from the list and put each alphabet in a list
#2.1 Initialize chances XD

chances = 10
used_letters = []

word = random.choice(words)

#3. Display the lengh of the word with the same number of dashes("_") 

dashes = ["_" for i in word]

while "_" in dashes:
    print(" ".join(dashes))
    
    #4. Ask the user to guess a letter
    #4.1 check if used_letter is empty
    if used_letters:
       print("Guessed letters:", ",".join(used_letters))
    guess = input(f"Chances left: {chances}\nGuess the letter: ").lower()
    #4.2 check if guess is one character and is a alphabetic character
    if len(guess) !=1 or not guess.isalpha():
       print("Invalid input, please use letters...")
       continue
    #4.3 check if guess is already used or not
    if guess in used_letters:
       print(f"You already used the letter '{guess}'")
       continue
    used_letters.append(guess)
    
    #5. if letter in word then replace the corresponding places(the dashes) with the letter

    if guess in word:
        print(f"You guessed '{guess}' correctly!")
        for index, letter in enumerate(word):
           if letter == guess:
              dashes[index] = guess

    #6. If letter not in word then show wrong guess and remove one chance
    
    else:
        chances-= 1
        if chances != 0:
            print(f"Wrong guess, you have {chances} chances left")

        #7. Once all the guesses are used, print "you lost!" and end the game
        else:
            print("You Lost!")
            print(f"The correct word is '{word}'")
            break
  
else:
   print(f"You Won!! You guessed the word: {word}")
