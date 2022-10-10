import random


randomNumber = random.randint(1, 100)

if randomNumber < 20:
    print("mini")
elif randomNumber > 20 & randomNumber < 80:
    print("medium")
elif randomNumber > 50:
    print("Large")