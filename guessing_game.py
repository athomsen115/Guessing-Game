import random

WIN_COUNT = 0
LOSS_COUNT = 0
GUESS_COUNT = 0
GAME_COUNT = 1

def end_game():
    print("Your final score was {} wins, {} losses".format(WIN_COUNT, LOSS_COUNT))
    
def guessing_game():
    global WIN_COUNT, LOSS_COUNT, GUESS_COUNT, GAME_COUNT
    while True:
        initiate_game = raw_input("Would you like to play a game? ").lower()
        WIN_COUNT = 0
        LOSS_COUNT = 0
        GUESS_COUNT = 0
        GAME_COUNT = 1
        if initiate_game.isalpha():
            if initiate_game == "yes" or initiate_game == "y":
                rand_int = random.randint(1,100)
                #print(rand_int)                                     # For testing purposes only
                print("I am thinking of a number between 1 and 100")
                print("You have 5 tries to guess my number")
                while GUESS_COUNT < 5:
                    guess = raw_input("What is your guess? ")
                    if guess.isdigit():
                        if int(guess) == rand_int:
                            print("Congratulations!! You Win!!")
                            GUESS_COUNT += 1
                            WIN_COUNT += 1
                            GAME_COUNT += 1
                            break
                        elif int(guess) < rand_int:
                            print("Sorry, your guess is too low.")
                            GUESS_COUNT += 1
                        elif int(guess) > rand_int:
                            print("Sorry, your guess is too high. ")
                            GUESS_COUNT += 1
                    else:
                        print("That is not a valid guess. Please enter a positive digit.")
                        GUESS_COUNT += 1
                GAME_COUNT += 1
                LOSS_COUNT += 1
                print("The correct answer was: {}".format(rand_int))
                while GAME_COUNT > 1 and GAME_COUNT <= 3:
                    initiate_game = raw_input("Do you want to play again? ").lower()
                    if initiate_game.isalpha():
                        if initiate_game == "yes" or initiate_game == "y":
                            rand_int = random.randint(1,100)
                            #print(rand_int)                                     # For testing purposes only
                            print("I am thinking of a number between 1 and 100")
                            print("You have 5 tries to guess my number")
                            GUESS_COUNT = 0
                            while GUESS_COUNT < 5:
                                guess = raw_input("What is your guess? ")
                                if guess.isdigit():
                                    if int(guess) == rand_int:
                                        print("Congratulations!! You Win!!")
                                        GUESS_COUNT += 1
                                        WIN_COUNT += 1
                                        GAME_COUNT += 1
                                        break
                                    elif int(guess) < rand_int:
                                        print("Sorry, your guess is too low. Guess Again. ")
                                        GUESS_COUNT += 1
                                    elif int(guess) > rand_int:
                                        print("Sorry, your guess is too high. Guess Again. ")
                                        GUESS_COUNT += 1
                                else:
                                    print("That is not a valid guess. Please enter a positive digit.")
                                    GUESS_COUNT += 1
                            print("The correct answer was: {}".format(rand_int))
                            GAME_COUNT += 1
                            LOSS_COUNT += 1
                        elif initiate_game == "no" or initiate_game == "n":
                            print("Okay. Goodbye!")
                            break
                        else:
                            print("That is not a valid response. Please enter yes or no.")
                            continue
                    else:
                        print("That is not a valid response. Please enter yes or no.")
                end_game()
            elif initiate_game == "no" or initiate_game == "n":
                print("Okay. Goodbye!")
                end_game()
            else:
                print("That is not a valid response. Please enter yes or no.")
                continue
        else:
            print("That is not a valid response. Please enter yes or no.")
            continue


guessing_game()