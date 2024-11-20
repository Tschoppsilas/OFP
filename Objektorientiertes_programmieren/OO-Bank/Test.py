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

    def konto_eröffnen(self):
        print(f"Sie haben ein {self.kontotyp} eröffnet. Ihr {self.kontotyp} hat die Kontonummer: {self.kontonummer}")

    @staticmethod
    def __fehlermeldungen(kontonummer, betrag=0):
        if kontonummer not in Konto.konten or Konto.konten[kontonummer]['aktiv'] == False:
            print(f"\033[91mFehler: Die Kontonummer {kontonummer} existiert nicht oder ist nicht aktiv.\033[0m")
            sys.exit()
        if betrag < 0:
            print(f"\033[91mFehler: Der Betrag muss positiv sein. Sie haben den Betrag {betrag} gewählt, welcher nicht "
                  f"zulässig ist.\033[0m")
            sys.exit()

    def bareinzahlung(self, betrag):
        self.__fehlermeldungen(self.kontonummer, betrag)
        self._aktualisiere_saldo(betrag)
        self._buchung_hinzufuegen(betrag, "Bareinzahlung")
        print("Die Bareinzahlung war erfolgreich.")

    def abhebung(self, betrag):
        self.__fehlermeldungen(self.kontonummer, betrag)
        if not self.kann_abbuchen(betrag):
            print(f"\033[91mFehler: Der Betrag {betrag} CHF kann nicht abgehoben werden. Maximales Guthaben: "
                  f"{self.saldo}.\033[0m")
            sys.exit()
        self._aktualisiere_saldo(-betrag)
        self._buchung_hinzufuegen(-betrag, "Abhebung")
        print(f"Der Betrag von {betrag} CHF wurde erfolgreich abgehoben.")

    def kontoübertrag(self, betrag, ziel_kontonummer, verwendungszweck=""):
        self.__fehlermeldungen(self.kontonummer, betrag)
        self.__fehlermeldungen(ziel_kontonummer, betrag)
        if not self.kann_abbuchen(betrag):
            print(f"\033[91mFehler: Der Betrag {betrag} CHF kann nicht abgebucht werden. Maximales Guthaben: "
                  f"{self.saldo}.\033[0m")
            sys.exit()

        # Gebühren berechnen und abbuchen
        self.gebuehren(betrag)

        # Betrag übertragen
        self.saldo -= betrag
        Konto.konten[self.kontonummer]['Saldo'] = self.saldo
        Konto.konten[ziel_kontonummer]['Saldo'] += betrag

        # Buchungen hinzufügen
        self._buchung_hinzufuegen(betrag, verwendungszweck, ziel_kontonummer)
        print(f"Übertrag von {betrag} CHF von Konto {self.kontonummer} auf Konto {ziel_kontonummer} abgeschlossen.")

    def gebuehren(self, betrag):
        if self.kontotyp != "Privatkonto":
            return
        gebuehren_prozent = 0.05  # Standardgebühr: 5%

        # Gebühren nur berechnen, wenn Betrag > 0
        if betrag <= 0:
            return
        gebuehrenbetrag = betrag * gebuehren_prozent
        gebuehrenkonto_nr = 0  # Gebührenkonto hat immer Kontonummer 0

        # Verhindern, dass Gebühren mehrmals abgezogen werden
        if not self.kann_abbuchen(gebuehrenbetrag + betrag):
            print(f"\033[91mFehler: Gebühren können nicht abgebucht werden. Saldo unzureichend.\033[0m")
            return

        # Gebühren abbuchen und auf das Gebührenkonto übertragen
        self.saldo -= gebuehrenbetrag
        Konto.konten[gebuehrenkonto_nr]['Saldo'] += gebuehrenbetrag

        # Gebühr buchen
        self._buchung_hinzufuegen(gebuehrenbetrag, f"Gebühren für Konto {self.kontonummer}")

        print(f"Gebühren von {gebuehrenbetrag} CHF für Konto {self.kontonummer} wurden auf das Gebührenkonto übertragen.")

    def _aktualisiere_saldo(self, betrag):
        """Hilfsmethode zum Aktualisieren des Saldo"""
        self.saldo += betrag
        Konto.konten[self.kontonummer]['Saldo'] = self.saldo

    def _buchung_hinzufuegen(self, betrag, verwendungszweck, empfaenger_konto=None):
        """Hilfsmethode zum Hinzufügen einer Buchung"""
        buchung = Buchung(betrag, datetime.datetime.now(), verwendungszweck, empfaenger_konto)
        self.buchungen.append(buchung)
        Konto.konten[self.kontonummer]['Buchungen'] = self.buchungen

    def abfrage_kontostand(self):
        self.__fehlermeldungen(self.kontonummer)
        print(f"Ihr Saldo beträgt: {self.saldo} CHF")

    def buchungsabfrage(self, anz_letzte_buchungen=1):
        self.__fehlermeldungen(self.kontonummer)
        buchungen = self.buchungen[-anz_letzte_buchungen:]
        for buchung in buchungen:
            print(f"Betrag: {buchung.betrag}, Datum: {buchung.datum}, Verwendungszweck: {buchung.verwendungszweck}, "
                  f"Übertragskontonummer: {buchung.empfänger_Konto}")

    @classmethod
    def alle_konten(cls):
        for kontonummer, konto_info in cls.konten.items():
            print(f"Kontonummer: {kontonummer}, Kontotyp: {konto_info['Kontotyp']}, Saldo: {konto_info['Saldo']}, "
                  f"Aktiv: {konto_info['aktiv']}")

    @classmethod
    def initialisiere_festgelegtes_konto(cls):
        if not cls.__festgelegtes_konto:  # Prüfen, ob das Konto bereits existiert
            cls.__festgelegtes_konto = Gebührenkonto()
            print(f"Das Gebührenkonto wurde erfolgreich initialisiert. Kontonummer: 0")
        else:
            print("Das Gebührenkonto wurde bereits initialisiert.")

    def kann_abbuchen(self, betrag):
        """
        Diese Methode sollte in jedem Kontotyp spezifisch implementiert werden.
        Sie prüft, ob der Betrag abgebucht werden kann (je nach Kontotyp).
        """
        raise NotImplementedError("Die Methode 'kann_abbuchen' muss in den abgeleiteten Klassen implementiert werden.")


# Abgeleitete Klassen für die Kontotypen

class Jugendkonto(Konto):
    def __init__(self):
        super().__init__("Jugendkonto")

    def kann_abbuchen(self, betrag):
        return self.saldo >= betrag


class Privatkonto(Konto):
    def __init__(self, limit=1000):
        super().__init__("Privatkonto")
        self.limit = limit

    def kann_abbuchen(self, betrag):
        return self.saldo + self.limit >= betrag


class Sparkonto(Konto):
    def __init__(self, zinssatz=0.02):
        super().__init__("Sparkonto")
        self.zinssatz = zinssatz

    def kann_abbuchen(self, betrag):
        return self.saldo >= betrag

    def zinsen_berechnen(self):
        """Berechnet die Zinsen auf das Sparkonto und aktualisiert den Saldo."""
        zinsen = self.saldo * self.zinss
