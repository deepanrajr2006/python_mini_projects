import random

choices=["rock","paper","scissor"]
while True:
    system_choice=random.choice(choices)
    user_input=input("Enter your choice(rock/paper/scissor): ").lower()
    if user_input not in choices:
        print("Invalid input(please enter valid input)")
        continue
    if system_choice==user_input:
        print("its tie")

    if system_choice=="rock" and user_input=="paper":
        print(f"System chose: {system_choice}\nYou chose: {user_input}")
        print("you won")

    elif system_choice=="rock" and user_input=="scissor":
        print(f"System chose: {system_choice}\nYou chose: {user_input}")
        print("System won")

    if system_choice=="paper" and user_input=="rock":
        print(f"System chose: {system_choice}\nYou chose: {user_input}")
        print("System won")

    if system_choice=="paper" and user_input=="scissor":
        print(f"System chose: {system_choice}\nYou chose: {user_input}")
        print("You won")

    if system_choice=="scissor" and user_input=="rock":
        print(f"System chose: {system_choice}\nYou chose: {user_input}")
        print("you won")

    if system_choice=="scissor" and user_input=="paper":
        print(f"System chose: {system_choice}\nYou chose: {user_input}")
        print("System won")


    play_again=input("if you want to play again(y/n):").lower()
    if play_again=="n":
        break

