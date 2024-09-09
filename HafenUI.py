import tkinter as tk
from tkinter import messagebox
import random

class Schiff:
    def __init__(self, name, laenge, geschwindigkeit, plastik, kapitänin):
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

class Kapitänin:
    def __init__(self, name):
        self.name = name

class Hafen:
    def __init__(self):
        self.kasse = 0
        self.schiffe = []

    def schiff_anlegen(self, schiff):
        if schiff.laenge >= 20:  # XXL-Schiff
            self.kasse += 750
            schiff.kasse-= 750
        else:
            self.kasse += 500
            schiff.kasse -= 500
        self.schiffe.append(schiff)
        print(f"{schiff.name} hat angelegt. Kasse des Hafens: {self.kasse} Euro") #f = formatierter string

    def schiff_verlassen(self, schiff):
        if schiff in self.schiffe:
            self.kasse -= 150
            self.schiffe.remove(schiff)
            schiff.kasse += 150
            print(f"{schiff.name} hat den Hafen verlassen. Pfangebühr 150€ zurück überwiesen")
            print(f"{schiff.name} hat einen Kontostand von {schiff.kasse}")

        else:
            print(f"{schiff.name} ist nicht im Hafen.")

    def schiff_liste_ausgeben(self):
        for schiff in self.schiffe:
            print(f"{schiff.name}")


käpitänin1 = Kapitänin("Ursula")
käpitänin2 = Kapitänin("Thomas")
käpitänin3 = Kapitänin("Elfriede")

# Objekte vom Typ Schiff erstellen (name, laenge, geschwindigkeit, plastik, kapitänin)
schiff1 = Schiff("Poseidon", 30, 17, 1700, käpitänin1)  # XXL-Schiff
schiff2 = Schiff("Calypso", 15, 18, 1800, käpitänin2)
schiff3 = Schiff("Neptune", 25, 25, 3000, käpitänin3)  # XXL-Schiff

# UI-Klasse
class SchiffUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hafen Management System")

        # Dropdown-Menü für die Auswahl des Schiffes
        self.schiff_var = tk.StringVar(master)
        self.schiff_dropdown = tk.OptionMenu(master, self.schiff_var, "Poseidon", "Calypso", "Neptune")
        self.schiff_dropdown.pack()

        # Button zum Anlegen eines Schiffes
        self.anlegen_button = tk.Button(master, text="Schiff anlegen", command=self.schiff_anlegen)
        self.anlegen_button.pack()

        # Button zum Verlassen eines Schiffes
        self.verlassen_button = tk.Button(master, text="Schiff verlassen", command=self.schiff_verlassen)
        self.verlassen_button.pack()

        # Button zum Plastikfischen
        self.fischen_button = tk.Button(master, text="Plastik fischen", command=self.plastik_fischen)
        self.fischen_button.pack()

        # Status Label
        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

        # Hafenobjekt erstellen
        self.hafen = Hafen()

        # Schiffe erstellen und im Hafen anlegen
        self.schiffe = {
            "Poseidon": Schiff("Poseidon", 30, 17, 1700, käpitänin1),
            "Calypso": Schiff("Calypso", 15, 18, 1800, käpitänin2),
            "Neptune": Schiff("Neptune", 25, 25, 3000, käpitänin3)
        }

        for schiff in self.schiffe.values():
            self.hafen.schiff_anlegen(schiff)

    def schiff_anlegen(self):
        schiff_name = self.schiff_var.get()
        schiff = self.schiffe[schiff_name]
        self.hafen.schiff_anlegen(schiff)
        self.status_label.config(text=f"{schiff.name} hat angelegt.")

    def schiff_verlassen(self):
        schiff_name = self.schiff_var.get()
        schiff = self.schiffe[schiff_name]
        self.hafen.schiff_verlassen(schiff)
        self.status_label.config(text=f"{schiff.name} hat den Hafen verlassen.")

    def plastik_fischen(self):
        schiff_name = self.schiff_var.get()
        schiff = self.schiffe[schiff_name]
        gefangenes_plastik = schiff.plastikFischen()
        if gefangenes_plastik > 0:
            messagebox.showinfo("Erfolg", f"{schiff.name} hat {gefangenes_plastik} kg Plastik gefischt.")
        else:
            messagebox.showwarning("Limit erreicht", f"{schiff.name} kann nicht mehr Plastik fischen, da das Limit erreicht ist.")
        self.status_label.config(text=f"{schiff.name} hat {schiff.plastik} kg Plastik an Bord.")

# Hauptprogramm
root = tk.Tk()
schiff_ui = SchiffUI(root)
root.mainloop()
