import random

sum = 0

while True:
    randomNumber1 = random.randint(10, 30)
    if randomNumber1 == 15 or randomNumber1 == 25:
        break

    sum = sum + randomNumber1
print(sum)

print("Zufallszahl war 15 oder 25")
print(randomNumber1)



