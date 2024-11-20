import datetime
import sys
from Test import Konto
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

    def Konto_schliessen(self, kontonummer):
        # Überprüfen, ob das Konto existiert
        if kontonummer in Konto.konten:
            # Überprüfen, ob der Kontostand 0 ist
            if Konto.konten[kontonummer]['Saldo'] == 0:
                # Konto auf inaktiv setzen
                Konto.konten[kontonummer]['aktiv'] = False
                print(f"Das Konto {kontonummer} wurde erfolgreich geschlossen.")
            else:
                print(f"\033[91mFehler: Konto kann nicht geschlossen werden, da der Kontostand {Konto.konten[kontonummer]['Saldo']} CHF beträgt.\033[0m")
        else:
            print(f"\033[91mFehler: Die Kontonummer {kontonummer} existiert nicht.\033[0m")

