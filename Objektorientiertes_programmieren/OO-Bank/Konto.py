import datetime
import sys
from Buchung import Buchung


class Konto:
    __letzte_kontonummer = 0  # Klassenvariable für die letzte vergebene Kontonummer
    konten = {}  # Klassenvariable für die Speicherung aller Konteninformationen
    __festgelegtes_konto = None

    def __init__(self, kontotyp):
        if type(self) is Konto:
            raise TypeError("Die Basisklasse 'Konto' kann nicht direkt instanziiert werden.")
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
        print(f"Vor der Einzahlung: {self.saldo} CHF")
        if betrag < 0:
            print(f"\033[91mFehler: Der Betrag muss positiv sein.\033[0m")
            return
        self.saldo += betrag  # Hier wird der Saldo des Sparkontos aktualisiert

        # Gebühren berechnen
        self.Gebühren(betrag)

        buchung = Buchung(betrag, datetime.datetime.now(), "Bareinzahlung")
        self.buchungen.append(buchung)
        print(f"Nach der Einzahlung: {self.saldo} CHF")

    def Kontoübertrag(self, betrag, ziel_kontonummer, verwendungszweck=""):
        if self.kontonummer not in Konto.konten or not self.aktiv:
            print(f"\033[91mFehler: Die Kontonummer {self.kontonummer} existiert nicht oder ist nicht aktiv.\033[0m")
            return
        if ziel_kontonummer not in Konto.konten or not Konto.konten[ziel_kontonummer]['aktiv']:
            print(
                f"\033[91mFehler: Die Zielkontonummer {ziel_kontonummer} existiert nicht oder ist nicht aktiv.\033[0m")
            return
        if self.kann_abbuchen(betrag):
            print(
                f"\033[91mFehler: Der Betrag {betrag} CHF kann nicht abgebucht werden. Maximales Guthaben: {self.saldo}.\033[0m")
            return

        # Gebühren berechnen und abbuchen
        self.Gebühren(betrag)

        # Betrag übertragen
        self.saldo -= betrag
        Konto.konten[ziel_kontonummer]['Saldo'] += betrag

        # Buchungen hinzufügen
        buchung = Buchung(betrag, datetime.datetime.now(), verwendungszweck, ziel_kontonummer)
        self.buchungen.append(buchung)
        buchung = Buchung(betrag, datetime.datetime.now(), verwendungszweck, self.kontonummer)
        Konto.konten[ziel_kontonummer]['Buchungen'].append(buchung)

        print(f"Übertrag von {betrag} CHF von Konto {self.kontonummer} auf Konto {ziel_kontonummer} abgeschlossen.")

    def Gebühren(self, betrag):
        gebühren_prozent = 0.05  # Standardgebühr: 5%

        if betrag <= 0:
            return

        gebührenbetrag = betrag * gebühren_prozent
        gebührenkonto_nr = 0  # Gebührenkonto hat immer Kontonummer 0

        if self.kontonummer not in Konto.konten or not self.aktiv:
            print(f"\033[91mFehler: Die Kontonummer {self.kontonummer} existiert nicht oder ist nicht aktiv.\033[0m")
            return

        # Überprüfen, ob der Saldo für die Gebühren ausreicht
        if not self.kann_abbuchen(gebührenbetrag + betrag):
            print(f"\033[91mFehler: Gebühren können nicht abgebucht werden. Saldo unzureichend.\033[0m")
            return

        # Gebühren abziehen
        self.saldo -= gebührenbetrag
        Konto.konten[gebührenkonto_nr]['Saldo'] += gebührenbetrag

        # Gebühr buchen
        buchung = Buchung(gebührenbetrag, datetime.datetime.now(), f"Gebühren für Konto {self.kontonummer}")
        self.buchungen.append(buchung)
        print(
            f"Gebühren von {gebührenbetrag} CHF für Konto {self.kontonummer} wurden auf das Gebührenkonto übertragen.")

    def abfrage_kontostand(self):
        if self.kontonummer not in Konto.konten or not self.aktiv:
            print(f"\033[91mFehler: Die Kontonummer {self.kontonummer} existiert nicht oder ist nicht aktiv.\033[0m")
            sys.exit()
        else:
            print(f"Ihr Saldo beträgt: {self.saldo} CHF")

    def Buchungsabfrage(self, anz_letzte_buchungen=1):
        if self.kontonummer in self.konten:
            buchungen = self.buchungen[-anz_letzte_buchungen:]
            for buchung in buchungen:
                print(
                    f"Betrag: {buchung.betrag}, Datum: {buchung.datum}, Verwendungszweck: {buchung.verwendungszweck}, Übertragskontonummer: {buchung.empfänger_Konto}")
        else:
            print(f"\033[91mFehler: Die Kontonummer {self.kontonummer} existiert nicht.\033[0m")
            sys.exit()

    @classmethod
    def alle_konten(cls):
        print(f"{cls.konten}")

    @classmethod
    def initialisiere_festgelegtes_konto(cls):
        if not cls.__festgelegtes_konto:  # Prüfen, ob das Konto bereits existiert
            cls.__festgelegtes_konto = Gebührenkonto()
            print(f"Das Gebührenkonto wurde erfolgreich initialisiert. Kontonummer: 0")
        else:
            print("Das Gebührenkonto wurde bereits initialisiert.")


class Jugendkonto(Konto):
    def __init__(self):
        super().__init__("Jugendkonto")

    def kann_abbuchen(self, betrag):
        return self.saldo >= betrag


class Privatkonto(Konto):
    __gebühren = 0.05

    def __init__(self, limit=1000):
        super().__init__("Privatkonto")
        self.limit = limit

    def kann_abbuchen(self, betrag):
        return self.saldo + self.limit >= betrag


class Sparkonto(Konto):
    def __init__(self):
        super().__init__("Sparkonto")

    def kann_abbuchen(self, betrag):
        return self.saldo >= betrag


class Gebührenkonto(Konto):
    def __init__(self):
        self.kontonummer = 0  # Feste Kontonummer zuweisen
        self.kontotyp = "Gebührenkonto"
        self.saldo = 0
        self.buchungen = []
        self.aktiv = True
        if self.kontonummer not in Konto.konten:
            Konto.konten[self.kontonummer] = {
                'Kontotyp': self.kontotyp,
                'Saldo': self.saldo,
                'Buchungen': self.buchungen,
                'aktiv': self.aktiv
            }


Konto.initialisiere_festgelegtes_konto()