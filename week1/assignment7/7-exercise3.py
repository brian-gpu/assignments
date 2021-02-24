import random

def play_game():
    random_value = random.randint(0, 9)
    is_guess_correct = False

    while is_guess_correct == False:
        guess = int(input("Guess a number:\n"))
        if guess == random_value:
            is_guess_correct = True
            print("Well guessed!")


play_game()