<<<<<<< HEAD
import random 
<<<<<<< HEAD
number = random.randint(1, 75) 
print("Guess a number between 1 and 75") 
=======
<<<<<<< HEAD
number = random.randint(1, 100) 
print("Guess a number between 1 and 100") 
guess = int(input()) 
if guess == number: 
 print("You win!") 
else: 
 print(f"Wrong! The number was {number}")
 
=======
number = random.randint(1, 50) 
print("Guess a number between 1 and 50") 
>>>>>>> a79716b4e1b72fab2bab44ced843650d89dcb66c
guess = int(input()) 
if guess == number: 
    print("You win!") 
else: 
    print(f"Wrong! The number was {number}") 
>>>>>>> 3d67c221552d653738ed33fecc9363e1d5f819c0
=======
import random
number = random.randint(1, 10)
print("Guess a number between 1 and 10")
guess = int(input())
if guess == number:
    print("You win!")
else:
    print(f"Wrong! The number was {number}")

import time
start_time = time.time()
print(f"Time taken: {time.time() - start_time:.2f} seconds")
>>>>>>> 64526cce33d594e98f8d814f0c9a2acd575fa8be
