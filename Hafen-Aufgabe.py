import random

class Schiff:
    def __init__(self, name, laenge, geschwindigkeit, kapitänin):
        self.name = name
        self.laenge = laenge
        self.kasse = 1000
        self.geschwindigkeit = geschwindigkeit # in Knoten
        self.plastik =0 # in KG
        self.kapitänin = kapitänin

    def plastikFischen(self):
        if self.plastik < 1000:
            gefangenes_plastik = random.randint(0, 1000 - self.plastik)  # Zufällige Menge an Plastik, ohne die Obergrenze zu überschreiten
            self.plastik += gefangenes_plastik
            print(f"{self.name} hat {gefangenes_plastik} kg Plastik gefischt. Insgesamt jetzt {self.plastik} kg an Bord.")
        else:
            print(f"{self.name} kann nicht mehr Plastik fischen, da das Limit erreicht ist.")

class Maskotchen:
    def __init__(self, name, sprüche:list[str]):
        self.name = name
        self.sprüche = sprüche

    def spruchAufsagen(self):
        print(random.choice(self.sprüche))




class Bankkonto:
    def __init__(self, kontostand):
        self.kontostand = kontostand

    def ueberweisung(self, volumen, sender, empfaenger):
        self.volumen = volumen
        print("Überweisung aufgerufen")
        print(volumen)
        print(sender)

        if sender >= volumen:
            sender = sender - volumen
            print(sender)
            empfaenger = empfaenger + volumen
            print(empfaenger)
        else:
            print("nicht genug Guthaben vorhanden")

        #print(sender.startguthaben)




class Kapitänin:
    def __init__(self, name, berufserfahrung, maskotchen:Maskotchen, bankkonto:Bankkonto):
        self.name = name
        self.berufserfahrung = berufserfahrung
        self.maskotchen = maskotchen
        self.bankkonto = bankkonto


class Hafen:
    def __init__(self, bankkonto:Bankkonto):
        self.bankkonto = bankkonto
        self.schiffe = []

    def schiff_anlegen(self, schiff):
        if schiff.laenge >= 20:  # XXL-Schiff
            self.bankkonto.kontostand += 750
            schiff.kapitänin.bankkonto.kontostand -= 750
        else:
            self.bankkonto.kontostand += 500
            schiff.kapitänin.bankkonto.kontostand -= 500
        self.schiffe.append(schiff)
        print(f"{schiff.name} hat angelegt. Kasse des Hafens: {self.bankkonto.kontostand} Euro") #f = formatierter string

    def schiff_verlassen(self, schiff):
        if schiff in self.schiffe:
            self.bankkonto.kontostand -= 150
            self.schiffe.remove(schiff)
            schiff.kapitänin.bankkonto.kontostand += 150
            print(f"{schiff.name} hat den Hafen verlassen. Pfangebühr 150€ zurück überwiesen")
            print(f"{schiff.name} hat einen Kontostand von {schiff.kapitänin.bankkonto.kontostand}")

        else:
            print(f"{schiff.name} ist nicht im Hafen.")

    def schiff_liste_ausgeben(self):
        for schiff in self.schiffe:
            print(f"{schiff.name}")


käpitänin1 = Kapitänin("Ursula", 7, Maskotchen("Ölefant", ["törööö", "blubb blubb blubb", "muhhh"]), Bankkonto(1500))
käpitänin2 = Kapitänin("Thomas", 4, Maskotchen("Jaguar", ["törööö", "blubb blubb blubb"]), Bankkonto(1500))
käpitänin3 = Kapitänin("Elfriede", 3, Maskotchen("Würmchen", ["törööö", "blubb blubb blubb"]), Bankkonto(1500))

# Objekte vom Typ Schiff erstellen (name, laenge, geschwindigkeit, plastik, kapitänin)
schiff1 = Schiff("Poseidon", 30, 17, käpitänin1)  # XXL-Schiff
schiff2 = Schiff("Calypso", 15, 18, käpitänin2)
schiff3 = Schiff("Neptune", 25, 25, käpitänin3)  # XXL-Schiff

print(schiff1.kapitänin.name)

# Hafenobjekt erstellen
hafen = Hafen(Bankkonto(5000))

# Schiffe im Hafen anlegen
#hafen.schiff_anlegen(schiff1)
#hafen.schiff_anlegen(schiff2)
#hafen.schiff_anlegen(schiff3)

#hafen.schiff_liste_ausgeben()
#hafen.schiff_verlassen(schiff1)
#hafen.schiff_liste_ausgeben()
#hafen.schiff_verlassen(schiff1)

schiff1.plastikFischen()
schiff2.plastikFischen()

#käpitänin1.maskotchen.spruchAufsagen()

print(schiff1.kapitänin.bankkonto.kontostand)
bankkonto=Bankkonto(500)
bankkonto.ueberweisung(100, schiff1.kapitänin.bankkonto, hafen.bankkonto)
print(hafen.bankkonto.kontostand)
print(schiff1.kapitänin.bankkonto.kontostand)

#print(schiff1.kapitänin.maskotchen.sprüche[0])