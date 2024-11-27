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
            'Kontonummer': self.kontonummer,
            'Kontotyp': self.kontotyp,
            'Saldo': self.saldo,
            'Buchungen': self.buchungen,
            'aktiv': self.aktiv
        }

    def Konto_eröffnen(self):
        print(f"Sie haben ein {self.kontotyp} eröffnet. Ihr {self.kontotyp} hat die Kontonummer: {self.kontonummer}")

    @staticmethod
    def __Fehlermeldungen(Kontonummer, betrag = 0):
        if Kontonummer not in Konto.konten or Konto.konten[Kontonummer]['aktiv'] == False:
            print(f"\033[91mFehler: Die Kontonummer {Kontonummer} existiert nicht oder ist nicht aktiv.\033[0m")
            sys.exit()
        if betrag < 0:
            print(
                f"\033[91mFehler: Der Betrag muss positiv sein. Sie haben den Betrag {betrag} gewählt, welcher nicht zulässig ist.\033[0m")
            sys.exit()


    def bareinzahlung(self, betrag):
        self.__Fehlermeldungen(self.kontonummer, betrag)
        # Betrag zur Saldo hinzufügen
        self.saldo += betrag

        # Die Änderung im Konto-Dictionary speichern
        Konto.konten[self.kontonummer]['Saldo'] = self.saldo

        # Buchung der Bareinzahlung
        buchung = Buchung(betrag, datetime.datetime.now(), "Bareinzahlung")
        self.buchungen.append(buchung)

        # Auch im Dictionary Buchung hinzufügen
        Konto.konten[self.kontonummer]['Buchungen'] = self.buchungen

        print("Die Bareinzahlung war erfolgreich.")

    def Kontoübertrag(self, betrag, ziel_kontonummer, verwendungszweck=""):
        self.__Fehlermeldungen(self.kontonummer, betrag)
        self.__Fehlermeldungen(ziel_kontonummer, betrag)
        if not self.kann_abbuchen(betrag):
            print(
                f"\033[91mFehler: Der Betrag {betrag} CHF kann nicht abgebucht werden. Maximales Guthaben: {self.saldo}.\033[0m")
            sys.exit()
        if self.kontotyp == "Privatkonto":
            # Gebühren berechnen und abbuchen
            self.Gebühren(betrag)

        # Betrag übertragen
        self.saldo -= betrag
        Konto.konten[self.kontonummer]['Saldo'] = self.saldo
        Konto.konten[ziel_kontonummer]['Saldo'] += betrag

        # Buchungen hinzufügen
        buchung = Buchung(betrag, datetime.datetime.now(), verwendungszweck, ziel_kontonummer)
        self.buchungen.append(buchung)
        buchung = Buchung(betrag, datetime.datetime.now(), verwendungszweck, self.kontonummer)
        Konto.konten[ziel_kontonummer]['Buchungen'].append(buchung)

        print(f"Übertrag von {betrag} CHF von Konto {self.kontonummer} auf Konto {ziel_kontonummer} abgeschlossen.")

    def Gebühren(self, betrag):
        if self.kontotyp != "Privatkonto":
            return
        gebühren_prozent = 0.05  # Standardgebühr: 5%

        # Gebühren nur berechnen, wenn Betrag > 0
        if betrag <= 0:
            return
        gebührenbetrag = betrag * gebühren_prozent
        gebührenkonto_nr = 0  # Gebühren_Zinskonto hat immer Kontonummer 0

        # Verhindern, dass Gebühren mehrmals abgezogen werden
        if not self.kann_abbuchen(gebührenbetrag + betrag):
            print(f"\033[91mFehler: Gebühren können nicht abgebucht werden. Saldo unzureichend.\033[0m")
            return

        # Direktes Abbuchen des Gebührenbetrags und Übertragen auf das Gebühren_Zinskonto
        self.saldo -= gebührenbetrag
        Konto.konten[gebührenkonto_nr]['Saldo'] += gebührenbetrag

        # Gebühr buchen
        buchung = Buchung(gebührenbetrag, datetime.datetime.now(), f"Gebühren für Konto {self.kontonummer}")
        self.buchungen.append(buchung)
        print(
            f"Gebühren von {gebührenbetrag} CHF für Konto {self.kontonummer} wurden auf das Gebühren_Zinskonto übertragen.")

    def abfrage_kontostand(self):
        self.__Fehlermeldungen(self.kontonummer)
        print(f"Ihr Saldo beträgt: {self.saldo} CHF")

    def Buchungsabfrage(self, anz_letzte_buchungen=1):
        self.__Fehlermeldungen(self.kontonummer)
        buchungen = self.buchungen[-anz_letzte_buchungen:]
        for buchung in buchungen:
            print(
                f"Betrag: {buchung.betrag}, Datum: {buchung.datum}, Verwendungszweck: {buchung.verwendungszweck}, Übertragskontonummer: {buchung.empfänger_Konto}")


    @classmethod
    def alle_konten(cls):
        for kontonummer, konto_info in cls.konten.items():
            print(
                f"Kontonummer: {kontonummer}, Kontotyp: {konto_info['Kontotyp']}, Saldo: {konto_info['Saldo']}, Aktiv: {konto_info['aktiv']}")

    @classmethod
    def initialisiere_festgelegtes_konto(cls):
        if not cls.__festgelegtes_konto:  # Prüfen, ob das Konto bereits existiert
            cls.__festgelegtes_konto = Gebühren_Zinskonto()
            print(f"Das Gebühren_Zinskonto wurde erfolgreich initialisiert. Kontonummer: 0")
        else:
            print("Das Gebühren_Zinskonto wurde bereits initialisiert.")


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
    __zinssatz = 0.02
    def __init__(self):
        super().__init__("Sparkonto")

    def kann_abbuchen(self, betrag):
        return self.saldo >= betrag

    def Zinssatz(self, Zinssatz = __zinssatz):
        gebühren_Zins_konto_nr = 0  # Gebühren / Zinskonto hat immer Kontonummer 0
        Zinsbetrag = self.saldo * Zinssatz
        # Direktes Abbuchen des Gebührenbetrags und Übertragen auf das Gebühren_Zinskonto
        self.saldo += Zinsbetrag
        Konto.konten[self.kontonummer]['Saldo'] = self.saldo
        Konto.konten[gebühren_Zins_konto_nr]['Saldo'] -= Zinsbetrag
        # Gebühr buchen
        buchung = Buchung(Zinsbetrag, datetime.datetime.now(), f"Zinsen für Konto {self.kontonummer}")
        self.buchungen.append(buchung)
        print(
            f"Der Zinsbetrag von {Zinsbetrag} CHF, wurde für das Konto mit der Nummer: {self.kontonummer} verbucht.")


class Gebühren_Zinskonto(Konto):
    def __init__(self):
        self.kontonummer = 0  # Feste Kontonummer zuweisen
        self.kontotyp = "Gebühren- und Zinskonto"
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