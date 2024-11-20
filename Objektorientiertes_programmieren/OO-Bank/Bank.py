import datetime
import sys
from Konto import Konto
from Buchung import Buchung
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

    @classmethod
    def konto_schliessen(cls, kontonummer):
        if kontonummer in Konto.konten:
            konto = Konto.konten[kontonummer]
            if konto['Saldo'] != 0:
                print(f"\033[91mFehler: Konto kann nicht geschlossen werden, da das Konto noch einen Restbetrag "
                      f"von {konto['Saldo']} CHF hat.\033[0m")
                sys.exit()
            else:
                konto['aktiv'] = False
                print(f"Das Konto {kontonummer} wurde erfolgreich geschlossen")
        else:
            print(f"\033[91mFehler: Die Kontonummer {kontonummer} existiert nicht.\033[0m")
            sys.exit()

