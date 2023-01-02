import random

def play_game():
    # guess the # game
    guess = input("Enter in your numerical guess. ")
    random_number = random.randint(0, 10)
    number_of_guess_left = 3
    # this is the main loop where the user gets 3 chances to guess the correct number 

    while number_of_guess_left > 0:
        if guess != random_number:
            number_of_guess_left -= 1
            print(f"The number {guess} was an incorrect guess. and you have {number_of_guess_left} guesses left ")
            guess = input("Enter in your numerical guess. ")
        elif number_of_guess_left == 0:
            print("You lose! You have no more chances left.")
        else:
            print("You Win! ")


while True:
    play_game()
    replay_input = input("Yes or No ").lower()
    if replay_input != "yes":
        break
