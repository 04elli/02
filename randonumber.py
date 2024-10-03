import random
while True:
  magicnumber=random.randint(1,100)
  guess = int(input("Enter your Guess"))

  if guess < magicnumber:
    print("Try again, It's Higher")
  elif guess > magicnumber: 
    print("Lower, Try again")
  else:
    print("You did it!")
  