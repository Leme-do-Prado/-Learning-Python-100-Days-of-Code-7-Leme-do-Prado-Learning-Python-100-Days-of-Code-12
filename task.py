import random

print("Welcome to the Number guessing game!\n I'm a number between 1 and 100.\n Guess me!")

play_game = True

while play_game==True:
    random_number = random.randint(1, 100)
    lives = 0

    player_choice = input("Choose a difficulty: 'easy' or 'hard'.\nEasy for 10 attempts,\nHard for 5 attempts.\n")

    if player_choice=='hard':
        lives=5
    elif player_choice=='easy':
        lives=10

    guess = int(input("What do you think the number is?\n"))

    while guess != random_number:
        if guess > random_number:
            print("Lower!")
            lives-=1
        elif random_number > guess:
            print("Higher!")
            lives-=1
        guess = int(input("What do you think the number is?\n"))

    if lives==0:
        print("...GAME OVER.\nYou lose!\n")
    else:
        print("\n...EXACTLY!\nYou win!\n")

    if input("Do you wish to play again?\n")=='yes':
        play_game = True
    else:
        play_game = False

print("\nThanks for playing!!!")
