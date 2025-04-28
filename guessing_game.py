import random
number=random.randint(1,100)
print("Guess a number between 1 and 100 ")
guess =int(input())
      
if guess==number:
 print("You Win")
else:

 print(f"wrong! The number was{number}")