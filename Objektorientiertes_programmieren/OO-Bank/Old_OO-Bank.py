import datetime
import sys

class Buchung:
    def __init__(self, betrag, datum, verwendungszweck, empfänger_Konto=None):
        self.betrag = betrag
        self.datum = datum
        self.verwendungszweck = verwendungszweck
        self.empfänger_Konto = empfänger_Konto

class Konto:
    __letzte_kontonummer = 0  # Klassenvariable für die letzte vergebene Kontonummer
    konten = {}  # Klassenvariable für die Speicherung aller Konteninformationen

    def __init__(self, kontotyp):
        Konto.__letzte_kontonummer += 1
        self.kontonummer = Konto.__letzte_kontonummer
        self.kontotyp = kontotyp
        self.saldo = 0
        self.buchungen = []
        self.aktiv = True
        Konto.konten[self.kontonummer] = {
            'Kontotyp': self.kontotyp,
            'Saldo': self.saldo,
            'Buchungen': self.buchungen,
            'aktiv': self.aktiv
        }

    def Konto_eröffnen(self):
        print(f"Sie haben ein {self.kontotyp} eröffnet. Ihr {self.kontotyp} hat die Kontonummer: {self.kontonummer}")

    def bareinzahlung(self, betrag):
        if self.kontonummer in Konto.konten and betrag > 0 and Konto.konten[self.kontonummer]['aktiv']:
            Konto.konten[self.kontonummer]['Saldo'] += betrag
            buchung = Buchung(betrag, datetime.datetime.now(), "Bareinzahlung")
            Konto.konten[self.kontonummer]['Buchungen'].append(buchung)
        else:
            if self.kontonummer not in Konto.konten or not Konto.konten[self.kontonummer]['aktiv']:
                print(f"\033[91mFehler: Die Kontonummer {self.kontonummer} existiert nicht oder ist nicht aktiv.\033[0m")
                sys.exit()
            else:
                print(f"\033[91mFehler: Der Betrag muss positiv sein. Sie haben den Betrag {betrag} gewählt, welcher nicht zulässig ist.\033[0m")
                sys.exit()

    def Kontoübertrag(self, betrag, ziel_kontonummer, verwendungszweck="Der Verwendungszweck wurde bei der Buchung nicht angegeben"):
        if self.kontonummer in Konto.konten or ziel_kontonummer in Konto.konten or betrag <= Konto.konten[self.kontonummer]['Saldo'] or Konto.konten[self.kontonummer]['aktiv'] or Konto.konten[ziel_kontonummer]['aktiv']:
            Konto.konten[self.kontonummer]['Saldo'] -= betrag
            Konto.konten[ziel_kontonummer]['Saldo'] += betrag
            buchung = Buchung(betrag, datetime.datetime.now(), verwendungszweck, ziel_kontonummer)
            Konto.konten[self.kontonummer]['Buchungen'].append(buchung)
            buchung = Buchung(betrag, datetime.datetime.now(), verwendungszweck, self.kontonummer)
            Konto.konten[ziel_kontonummer]['Buchungen'].append(buchung)
            print(f"Der Übertrag von {betrag} CHF vom Konto {self.kontonummer} zum Konto {ziel_kontonummer} wurde verbucht")
        else:
            if self.kontonummer not in Konto.konten or not Konto.konten[self.kontonummer]['aktiv']:
                print(f"\033[91mFehler: Die Kontonummer {self.kontonummer} existiert nicht oder ist nicht aktiv.\033[0m")
                sys.exit()
            if ziel_kontonummer not in Konto.konten or not Konto.konten[ziel_kontonummer]['aktiv']:
                print(f"\033[91mFehler: Die Kontonummer {ziel_kontonummer} existiert nicht oder ist nicht aktiv.\033[0m")
                sys.exit()
            else:
                print(f"\033[91mFehler: Der Betrag ist zu groß. Der maximale Betrag ist {Konto.konten[self.kontonummer]['Saldo']}.\033[0m")
                sys.exit()

    @classmethod
    def abfrage_kontostand(cls, kontonummer):
        if kontonummer not in Konto.konten or not Konto.konten[kontonummer]['aktiv']:
            print(f"\033[91mFehler: Die Kontonummer {kontonummer} existiert nicht oder ist nicht aktiv.\033[0m")
            sys.exit()
        else:
            print(f"Ihr Saldo beträgt: {Konto.konten[kontonummer]['Saldo']} CHF")

    @classmethod
    def Buchungsabfrage(cls, kontonummer, anz_letzte_buchungen=1):
        if kontonummer in cls.konten:
            buchungen = cls.konten[kontonummer]['Buchungen'][-anz_letzte_buchungen:]
            for buchung in buchungen:
                print(f"Betrag: {buchung.betrag}, Datum: {buchung.datum}, Verwendungszweck: {buchung.verwendungszweck}, Übertragskontonummer: {buchung.empfänger_Konto}")
        else:
            print(f"\033[91mFehler: Die Kontonummer {kontonummer} existiert nicht.\033[0m")
            sys.exit()

    @classmethod
    def alle_konten(cls):
        print(f"{cls.konten}")

class Bank:

    @staticmethod
    def Buchungs_journal(kontonummer, anz_letzte_buchungen=1):
        if kontonummer in Konto.konten:
            buchungen = Konto.konten[kontonummer]['Buchungen'][-anz_letzte_buchungen:]
            for buchung in buchungen:
                print(f"Betrag: {buchung.betrag}, Datum: {buchung.datum}, Verwendungszweck: {buchung.verwendungszweck}, Übertragskontonummer: {buchung.empfänger_Konto}")
        else:
            print(f"\033[91mFehler: Die Kontonummer {kontonummer} existiert nicht.\033[0m")
            sys.exit()

    def Konto_schliessen(self, kontonummer):
        if kontonummer in Konto.konten:
            if Konto.konten[kontonummer]['Saldo'] != 0:
                print(f"\033[91mFehler: Konto kann nicht geschlossen werden, da das Konto noch einen Restbetrag von {Konto.konten[kontonummer]['Saldo']} CHF hat.\033[0m")
                sys.exit()
            else:
                Konto.konten[kontonummer]['aktiv'] = False
                print(f"Das Konto {kontonummer} wurde erfolgreich geschlossen")
        else:
            print(f"\033[91mFehler: Die Kontonummer {kontonummer} existiert nicht.\033[0m")
            sys.exit()
