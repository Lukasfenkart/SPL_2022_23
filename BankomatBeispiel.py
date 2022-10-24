Konto = 0
betrag = 0

while True:
    eingabe = input("Was wollen sie machen Einzahlen, Auszahlen, Kontostand, Beenden ")
    
    if eingabe == "Einzahlen":
        betrag = int(input())
        Konto = Konto + betrag
        print("eingezahlt" , betrag)
    elif eingabe == "Auszahlen":
        betrag = int(input())
        if betrag > Konto:
            print("zu wenig Geld")
        else:
            Konto = Konto - betrag
            print("ausgezahlt" , betrag)
    elif eingabe == "Kontostand":
        print(Konto)
    elif eingabe == "Beenden":
        print("Beendet")
        break
