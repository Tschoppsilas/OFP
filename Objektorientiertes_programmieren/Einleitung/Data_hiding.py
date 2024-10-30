class Kunde:
    #Data Hiding des Zinssatzes
    zins = 0.025
    def __init__(self, vorname, nachname, saldo=0):
        self.vorname = vorname
        self.nachname = nachname
        self.saldo = saldo

    def einzahlen(self, betrag):
        self.saldo += betrag

    def abheben(self, betrag):
        if betrag > self.saldo:
            raise ValueError("Nicht genügend Guthaben")
        self.saldo -= betrag

    def zahle_zinsen(self):
        self.saldo = self.saldo * (1+Kunde.zins)

Kunde1 = Kunde("Max", "Mustermann", 2000)
Kunde1.zahle_zinsen()
print(Kunde1.saldo)