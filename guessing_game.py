mport random

def guessing_game():
    while True:
        initiate_game = input("Would you like to play a game? ").lower()
        if initiate_game.isalpha():
            if initiate_game == "yes" or initiate_game == "y":
                count = 0
                rand_int = random.randint(1,100)
                print(rand_int)                                     # For testing purposes only
                print("I am thinking of a number between 1 and 100")
                guess = input("What is your guess? ")
                # SANITIZE USER INPUT
                while count >= 3:
                    #PLAY GAME!!
                elif initiate_game == "no" or initiate_game == "n":
                    break
                else:
                    print("That is not a valid response. Please enter yes or no.")
                    continue
