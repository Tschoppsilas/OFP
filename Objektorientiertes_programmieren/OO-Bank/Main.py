import datetime
import sys
from Konto import Konto, Jugendkonto, Sparkonto, Privatkonto
from Bank import Bank
from Buchung import Buchung

# Instanziierung von Objekten
privatkonto = Privatkonto()  # Privatkonto mit Standardlimit
Jugendkonto1 = Jugendkonto()  # Jugendkonto 1
Jugendkonto2 = Jugendkonto()  # Jugendkonto 2
sparkonto = Sparkonto()  # Sparkonto mit Standardzinssatz

# Bareinzahlung auf die Konten
print("Bareinzahlung auf Jugendkonto2:")
Jugendkonto2.bareinzahlung(2000)
print("\nBareinzahlung auf Privatkonto:")
privatkonto.bareinzahlung(1000)

# Zeige alle Konten und deren Salden
print("\nAlle Konten und Salden:")
Konto.alle_konten()

# Kontoübertrag durchführen (übertrage 300 CHF von Jugendkonto2 zu einem anderen Konto)
print("\nKontoübertrag (300 CHF von Jugendkonto2 auf Privatkonto):")
Jugendkonto2.Kontoübertrag(300, privatkonto.kontonummer, "Testüberweisung Jugendkonto2 -> Privatkonto")

# Zeige den aktuellen Kontostand des Gebührenkontos (Kontonummer 0)
print(f"\nGebührenkonto (Kontonummer 0) Saldo: {Konto.konten[0]['Saldo']}")

# Kontoübertrag (von Privatkonto auf Sparkonto)
print("\nKontoübertrag (200 CHF von Privatkonto auf Sparkonto):")
privatkonto.Kontoübertrag(200, sparkonto.kontonummer, "Testüberweisung Privatkonto -> Sparkonto")

# Abfrage des Kontostands des Gebührenkontos (Kontonummer 0)
print(f"\nAktualisierter Saldo des Gebührenkontos (Kontonummer 0): {Konto.konten[0]['Saldo']}")

# Buchungsabfrage
print("\nBuchungsabfrage für Jugendkonto2:")
Jugendkonto2.Buchungsabfrage(2)  # Abfrage der letzten 2 Buchungen auf Jugendkonto2
print("\nBuchungsabfrage für Privatkonto:")
privatkonto.Buchungsabfrage(2)  # Abfrage der letzten 2 Buchungen auf Privatkonto

# Konto schließen (Versuch, Konto 1 zu schließen)
print("\nVersuch, Konto 1 zu schließen:")
Bank.konto_schliessen(2)

# Zeige alle Konten und deren Salden nach den Operationen
print("\nAlle Konten nach den Operationen:")
Konto.alle_konten()

