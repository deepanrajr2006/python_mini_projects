import random
count=3
for i in range(3):
    guess=random.randint(1,10)
    choice=int(input("Enter your number(1 to 10):"))
    if choice==guess:
        print("Congratulation you won the game")
        break
    else:
        count -=1
        print(f"you lose the game,And you have {count} attempts only")

print("Better luck next time")
