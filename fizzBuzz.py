def fizzbuzz(obergrenze):
    for zahl in range(1, obergrenze + 1):
        if zahl % 3 == 0 and zahl % 5 == 0:
            print("FizzBuzz")
        elif zahl % 3 == 0:
            print("Fizz")
        elif zahl % 5 == 0:
            print("Buzz")
        else:
            print(zahl)


try:                                                                                # Benutzer gibt die Obergrenze ein
    obergrenze = int(input("Bitte gib die Obergrenze ein: "))                       # Zahleneingabe in Console
    fizzbuzz(obergrenze)
except ValueError:                                                                  # wenn Kommazahl dann Fehler / muss immer eine Bedingung definieren wenn Try ins leere läuft
   print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")                       #definieren was passiert wenn