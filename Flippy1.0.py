import random
import time

# This is the guessing totals, can call at the end
incorrect_guesses = 0
correct_guesses = 0
total_guesses = correct_guesses + incorrect_guesses

# logic
wait = time.sleep(1.5)

#Resets and Restarts the game
bootup = True
playing_count = 0

while playing_count < 5:
    while bootup:
        print("Welcome to Flippy 1.0V")
        print("") 
        print("Please enter your guess!")
        guess = str(input())
        coin = random.choice(["Heads", "Tails"])
        if guess == ("Heads") or ("Tails"):
            print("You have choosen :", guess, "!")
            time.sleep(3)
            print("The coin has flipped!")
            print(coin)
            if coin == guess:
                print("You have guessed correctly!")
                print("Well Done!")
                correct_guesses += 1
            if coin != guess:
                print("Sadly, you have guessed incorrectly")
                print("Better luck next time!")
                incorrect_guesses += 1
        else:
            print("Please type Heads or Tails!")
            break
        time.sleep(3)
        print("")
        print("You have guessed ", total_guesses, "times!")
        print("You have won", correct_guesses, "number of times")
        print("")
        print("Your current win/lose percentage is ", "I havent got that far yet")
        print("")
        time.sleep(3)
        print("Would you like to continue playing?")
        print("Please enter y or n")
        playing = str(input())
        if playing == "y":
            playing_count += 1
            continue
        if playing == "n":
            bootup = False
        break
print("Thank you for playing Flippy!")
time.sleep(3)
bootup = True    

