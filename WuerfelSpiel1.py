import random
sum = 0
sum2 = 0
print("ready to lose? Yes or No")
start = input()
if start == "No":
    print("Beendet")
else:
    for i in range(0,6):
        randomNumber1 = random.randint(1, 6)
        sum = sum + randomNumber1
    for i in  range(0,6):
        print("Würfeln sie, schreiben sie w")
        wuerfel = (input())
        if wuerfel == "w":
            randomNumber2 = random.randint(1, 6)
            print("du hast eine", randomNumber2, "gewürfelt")
        sum2 = sum + randomNumber2

    if sum > sum2:
        print("Computer hat gewonnen mit ", sum, " du hast ", sum2)
    else:
        print("Du hast gewonnen mit ", sum2, "der Computer hat", sum)