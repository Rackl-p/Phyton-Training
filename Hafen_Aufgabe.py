import random

class Schiff:
    def __init__(self, name, laenge, geschwindigkeit, kapitänin):
        self.name = name
        self.laenge = laenge
        self.geschwindigkeit = geschwindigkeit  # in Knoten
        self.plastik = 0  # in KG
        self.kapitänin = kapitänin

    def plastikFischen(self):
        if self.plastik < 1000:
            gefangenes_plastik = random.randint(0, 1000 - self.plastik)
            self.plastik += gefangenes_plastik
            print(f"{self.name} hat {gefangenes_plastik} kg Plastik gefischt. Insgesamt jetzt {self.plastik} kg an Bord.")
        else:
            print(f"{self.name} kann nicht mehr Plastik fischen, da das Limit erreicht ist.")

class Maskotchen:
    def __init__(self, name, sprüche):
        self.name = name
        self.sprüche = sprüche

    def spruchAufSagen(self):
        print(random.choice(self.sprüche))

class Bankkonto:
    def __init__(self, kontostand):
        self.kontostand = kontostand

    def überweisen(self, volumen, empfängerKonto):
        if self.kontostand >= volumen:
            self.kontostand -= volumen
            empfängerKonto.kontostand += volumen
            return True
        else:
            return False

class Kapitänin:
    def __init__(self, name, berufserfahrung, maskotchen, bankkonto):
        self.name = name
        self.berufserfahrung = berufserfahrung
        self.maskotchen = maskotchen
        self.bankkonto = bankkonto

class Hafen:
    def __init__(self, bankkonto):
        self.bankkonto = bankkonto
        self.schiffe = []

    def schiffAufnehmen(self, schiff):
        if self.bankkonto.kontostand >= 150:
            self.bankkonto.kontostand -= 150
            self.schiffe.append(schiff)
            print(f"{schiff.name} wurde im Hafen aufgenommen.")
            return True
        else:
            print(f"{schiff.name} konnte nicht aufgenommen werden. Nicht genug Guthaben im Hafenkonto.")
            return False

    def plastikEinkaufen(self, schiff):
        if schiff.plastik >= 10:
            überweisungsbetrag = schiff.plastik // 10
            if self.bankkonto.überweisen(überweisungsbetrag, schiff.kapitänin.bankkonto):
                schiff.plastik = 0
                print(f"{schiff.name} hat {überweisungsbetrag} Euro für das Plastik erhalten.")
                return True
            else:
                print(f"Überweisung fehlgeschlagen. Nicht genug Guthaben im Hafenkonto.")
                return False
        else:
            print(f"{schiff.name} hat nicht genug Plastik zum Verkauf.")
            return False

    def schiffVerabschieden(self, schiff):
        if schiff in self.schiffe:
            self.schiffe.remove(schiff)
            schiff.kapitänin.maskotchen.spruchAufSagen()
            print(f"{schiff.name} hat den Hafen verlassen.")
        else:
            print(f"{schiff.name} ist nicht im Hafen.")

    def schnellstesSchiffFinden(self):
        return max(self.schiffe, key=lambda x: x.geschwindigkeit)

    def schlauestesMaskottchenFinden(self):
        return max(self.schiffe, key=lambda x: len(x.kapitänin.maskotchen.sprüche))

    def schiffeAnzeigen(self):
        sorted_schiffe = sorted(self.schiffe, key=lambda x: x.kapitänin.berufserfahrung, reverse=True)
        for schiff in sorted_schiffe:
            print(f"{schiff.name} (Kapitän: {schiff.kapitänin.name}, Erfahrung: {schiff.kapitänin.berufserfahrung} Jahre)")


# Beispielverwendung:

maskottchen1 = Maskotchen("Ölefant", ["törööö", "blubb blubb blubb", "muhhh"])

konto1 = Bankkonto(700)

kapitänin1 = Kapitänin("Ursula", 7, maskottchen1, konto1)

schiff1 = Schiff("Poseidon", 30, 17, kapitänin1)

hafen = Hafen(Bankkonto(2000))

hafen.schiffAufnehmen(schiff1)

schiff1.plastikFischen()

hafen.plastikEinkaufen(schiff1)

schnellstes_schiff = hafen.schnellstesSchiffFinden()
print(f"Schnellstes Schiff: {schnellstes_schiff.name}")

schlauestes_maskottchen = hafen.schlauestesMaskottchenFinden()
print(f"Schlauestes Maskottchen: {schlauestes_maskottchen.kapitänin.maskotchen.name}")

print("Schiffe im Hafen:")
hafen.schiffeAnzeigen()
