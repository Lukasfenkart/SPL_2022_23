
import random


randomNumber1 = random.randint(1, 100)
randomNumber2 = random.randint(1, 100)

print(randomNumber1)
print(randomNumber2)

if randomNumber1 < randomNumber2 and randomNumber1 < 50:
    print("Zahl 1 ist kleiner als Zahl 2 und Mini")
elif randomNumber1 < 30 or randomNumber2 < 30:
 print("Eine der beiden Zahlen ist kleiner als 30")
elif randomNumber1 < 50 and not randomNumber2 == 50:
    print("Erste Zahl klein, zweite kein 50iger")