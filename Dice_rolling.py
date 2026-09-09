import random

while True:
   chioce=input("If you want to spin the dice: (Yes/no) ").lower()
   if chioce=="yes": 
      die1=random.randint(1,6)
      die2=random.randint(1,6)
      print(f"{die1},{die2}")
   elif chioce=="no":
      print("Thanks for playing")
      break
   else:
      print("Invalid input")

