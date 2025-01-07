from datetime import datetime

class Bank:
    def __init__(self):
        self.__konten = {}
        self.__next_kontonummer = 1
        self.__bank_journal = []
        self.__KundenID = {}
        self.__next_kundennummer = 1

        # Bank hat ein eigenes Konto (z.B. für Gebühren oder interne Buchungen)
        self.bank_konto = Bankkonto(konto_id=0, inhaber="Bank")
        self.__konto_id=0
        self.__konten[self.__konto_id] = self.bank_konto
        print("Bankkonto erstellt.")

    def erstelle_entnehme_KundenID(self, vorname, nachname, geburtsdatum):
        Kunde = (vorname, nachname, geburtsdatum)
        if Kunde not in self.__KundenID:
            Kundennummer = self.__next_kundennummer
            self.__next_kundennummer += 1
            self.__KundenID[Kunde] = Kundennummer
            return Kundennummer
        else:
            return self.__KundenID[Kunde]

    def Konto_eröffnen(self, Kontotyp, Vorname, Nachname, geburtsdatum, limit = None):
        Kunden_ID = self.erstelle_entnehme_KundenID(Vorname, Nachname, geburtsdatum)
        if Kunden_ID not in self.__konten:
            self.__konten[Kunden_ID] = []
        konto_nummer = self.__next_kontonummer
        self.__next_kontonummer += 1
        Kontotyp(konto_nummer, Vorname, Nachname, geburtsdatum, limit)
        konto = Kontotyp(konto_nummer, Vorname, Nachname, geburtsdatum, limit)
        self.__konten[Kunden_ID].append(konto)
        return konto

    def Buchung(self, start_konto_id, ziel_konto_id, betrag, zweck):
        if start_konto_id not in self.__konten:  # kontrolliere, ob abbuchendes Konto existiert
            raise ValueError("Ihr Konto wurde nicht gefunden")
        elif ziel_konto_id not in self.__konten:  # kontrolliere, ob zubuchendes Konto existiert
            raise ValueError("Das Zielkonto wurde nicht gefunden")
        start_konto_id = self.__konten[start_konto_id][0]
        ziel_konto_id = self.__konten[ziel_konto_id][0]
        start_konto_id.buchen(-betrag, gegenkonto=ziel_konto_id, verwendungszweck=zweck)
        ziel_konto_id.buchen(betrag, gegenkonto=start_konto_id, verwendungszweck=zweck)
        self.__bank_journal.append({
            'zeit': datetime.now(),
            'von': start_konto_id,
            'zu': ziel_konto_id,
            'betrag': betrag,
            'zweck': zweck
        })

    def get_Bankjournal(self, max_einträge=None):
        return self.__bank_journal[-max_einträge:] if max_einträge else self.__bank_journal

    def get_konto_info(self, kontonummer):
        # Iteriere durch alle Kunden und deren Konten
        for Kunden_ID, konten in self.__konten.items():
            # Wenn es nur ein einzelnes Konto gibt, dann kann es direkt ohne Schleife gefunden werden
            for konto in konten:
                if konto.get_Konto_ID() == kontonummer:  # Überprüfung der Konto-ID
                    return konto
        raise ValueError(f"Konto mit der Nummer {kontonummer} nicht gefunden")

    def Konto_schliessen(self, kontonummer):
        for Kunden_ID, konten in self.__konten.items():
            for konto in konten:
                if konto["Kontonummer"] == kontonummer:
                    if konto.get("geschlossen", False):  # Prüfen, ob das Konto bereits geschlossen ist
                        raise ValueError(f"Konto {kontonummer} ist bereits geschlossen.")

                    # Überprüfen, ob das Konto noch offene Buchungen hat
                    if konto["Kontotyp"].get_saldo() != 0:
                        raise ValueError(f"Konto {kontonummer} hat noch ein nicht ausgeglichenes Saldo und kann nicht geschlossen werden.")

                    # Wenn keine offenen Buchungen vorhanden sind und das Saldo 0 ist, kann das Konto geschlossen werden
                    konto["geschlossen"] = True  # Konto als geschlossen markieren
                    return True

        raise ValueError("Kontonummer nicht gefunden")


class Konto:
    def __init__(self, Konto_ID, Vorname, Nachname, geburtsdatum, limit):
        self.__Konto_ID = Konto_ID
        self.__Kunde = (Vorname, Nachname, geburtsdatum)
        self.__saldo = 0.0
        self.__buchungsjournal = []
        self.limit = limit

    def get_Konto_ID(self):
        return self.__Konto_ID  # Getter für Konto_ID

    def get_Kunde(self):
        return self.__Kunde

    def Bareinzahlung(self, betrag):
        if betrag > 0:
            self.__saldo += betrag
            self.__buchungsjournal.append({
                'zeit': datetime.now(),
                'betrag': betrag,
                'gegenkonto': None,
                'zweck': 'Einzahlung'
            })
        else:
            raise ValueError("Einzahlungsbetrag muss grösser 0 sein.")

    def get_saldo(self):
        return self.__saldo

    def get_journal(self, max_einträge=None):
        return self.__buchungsjournal[-max_einträge:] if max_einträge else self.__buchungsjournal

    def buchen(self, betrag, zu=None, zweck=""):
        # Allgemeine Buchung für alle Konten
        self.__saldo += betrag
        self.__buchungsjournal.append({
            'zeit': datetime.now(),
            'betrag': betrag,
            'gegenkonto': zu,
            'zweck': zweck
        })


class Jugendkonto(Konto):
    def __init__(self, Konto_ID, Vorname, Nachname, geburtsdatum, limit):
        super().__init__(Konto_ID, Vorname, Nachname, geburtsdatum, limit)#greift auf Elternklasse (Konto) zu


    def buchen(self, betrag, zu=None, zweck="Bareinzahlung"):
        if self.get_saldo() + betrag < 0:
            raise ValueError("Das Jugendkonto darf nicht ins Minus gehen!")
        super().buchen(betrag, zu, zweck)


class Privatkonto(Konto):
    def __init__(self, Konto_ID, Vorname, Nachname, geburtsdatum, limit):
        super().__init__(Konto_ID, Vorname, Nachname, geburtsdatum, limit)#greift auf Elternklasse (Konto) zu


    def buchen(self,betrag, zu=None, zweck = "Bareinzahlung" ):
        if self.get_saldo() + betrag < 0 - self.limit:
            raise ValueError("Das Jugendkonto darf nicht ins Minus gehen!")
        if betrag < 0:
            Bankgebühr = betrag * 0.05
            Bank.Buchung(start_konto_id=self.__Konto_ID, ziel_konto_id= 0, betrag=Bankgebühr, zweck="Bankgebühr")
        else:
            super().buchen(betrag, zu, zweck)


class Sparkonto(Konto):

    def __init__(self, Konto_ID, Vorname, Nachname, geburtsdatum, limit):
        super().__init__(Konto_ID, Vorname, Nachname, geburtsdatum, limit)#greift auf Elternklasse (Konto) zu

    def buchen(self, betrag, zu=None, zweck = "Bareinzahlung"):
        if self.get_saldo() + betrag < 0:
            raise ValueError("Das Jugendkonto darf nicht ins Minus gehen!")
        super().buchen(betrag, zu, zweck)


    def Zinsen(self):
        Zinssatz = 0.0025
        zinsen_betrag = self.get_saldo() * Zinssatz
        Bank.Buchung(start_konto_id=self.__Konto_ID, ziel_konto_id=0, betrag=zinsen_betrag, zweck="Zinsen")

class Bankkonto(Konto):
    def __init__(self, konto_id, inhaber):
        super().__init__(konto_id, inhaber, "", "", None)  # Bankkonto braucht kein Limit

    def buchen(self, betrag, zu=None, zweck="Geschenk"):
        super().buchen(betrag, zu, zweck)