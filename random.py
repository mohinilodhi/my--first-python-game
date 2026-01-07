import random

secret_number = random.randint(1, 100)

while True:
  user = int(input("Guess the number (1-100): "))
  
  if user == secret_number:
    print("Congratulations you are correct")
    break
  elif user < secret_number:
    print("Too low, try again")
  else:
    print("Too high, try again")
 