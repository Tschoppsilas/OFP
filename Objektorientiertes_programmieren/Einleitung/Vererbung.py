class Kunde:
    def __init__(self, Vorname, Nachname, Saldo = 0):
        self.vorname = Vorname
        self.nachname = Nachname
        self.saldo = Saldo

    def einzahlen(self, betrag):
        self.saldo += betrag

    def abheben(self, betrag):
        if betrag > self.saldo:
            raise ValueError("Nicht genügend Guthaben")
        self.saldo -= betrag

class PrivatKunde(Kunde):
    def __init__(self, Vorname, Nachname, Saldo, Termine=None):
        super().__init__(Vorname, Nachname, Saldo) #Ruft die Kunden Klasse auf und holt die Werte von dort
        if Termine is None:
            self.termine = []
        else:
            self.termine = Termine

    def mache_termine(self, termin):
        self.termine.append(termin)

pkunde1 = PrivatKunde("Max", "Mustermann", Saldo = 1000)
pkunde1.mache_termine("31-10-2024")
pkunde1.mache_termine("31-12-2024")

print(pkunde1.__dict__)