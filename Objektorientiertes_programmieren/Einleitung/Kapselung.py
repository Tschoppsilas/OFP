class Konto:
    def __init__(self, kontonummer, saldo):
        self.kontonummer = kontonummer
        self.saldo = saldo

    def einzahlen(self, betrag):
        self.saldo += betrag

    def abheben(self, betrag):
        if betrag > self.saldo:
            raise ValueError("Nicht genügend Guthaben")
        self.saldo -= betrag

Kunde1 = Konto(112254, 2000)
Kunde2 = Konto(112254, 2001)

Kunde1.abheben(100)

print(Kunde1.saldo)
