import datetime
import sys
from Test import Konto, Jugendkonto, Sparkonto, Privatkonto  # Achte darauf, dass alle Konten importiert sind
from Bank import Bank
from Buchung import Buchung

# Instanziierung von Objekten
privatkonto = Privatkonto()
jugendkonto1 = Jugendkonto()
jugendkonto2 = Jugendkonto()
Sparkonto = Sparkonto()
Bank = Bank()

# Bareinzahlung durchführen
print("Bareinzahlung auf Jugendkonto 2 und Privatkonto:")
jugendkonto2.bareinzahlung(2000)  # Einzahlung auf Jugendkonto2
privatkonto.bareinzahlung(1000)  # Einzahlung auf Privatkonto
Sparkonto.bareinzahlung(1000)  # Einzahlung auf Sparkonto
Konto.alle_konten()  # Alle Konten anzeigen

# Kontoübertrag durchführen
print("\nDurchführung von Kontoüberträgen:")
jugendkonto2.Kontoübertrag(300, 1, "Testüberweisung")  # Übertrag von Jugendkonto2 auf Konto 2
privatkonto.Kontoübertrag(800, 3, "Testüberweisung")  # Übertrag von Privatkonto auf Konto 2
Sparkonto.Kontoübertrag(200, 3, "Testüberweisung")

# Abfrage des Kontostands des Gebührenkontos (Kontonummer 0)
print("\nAktueller Kontostand des Gebührenkontos (Kontonummer 0):")
print(Konto.konten[0]['Saldo'])  # Gebühren_Zinskonto (Kontonummer 0)

# Buchungsabfrage
print("\nBuchungsabfrage für Jugendkonto 2 und Privatkonto (letzte Buchung):")
jugendkonto2.Buchungsabfrage(1)  # Abfrage der letzten Buchung auf Jugendkonto2
privatkonto.Buchungsabfrage(1)   # Abfrage der letzten Buchung auf Privatkonto

# Alle Konten anzeigen
print("\nAlle Konten anzeigen:")
Konto.alle_konten()  # Zeigt alle Konten an

print("\nVersuche, ein Konto zu schließen:")
Bank.Konto_schliessen(2)

print("\nZinsen verbuchen")
Sparkonto.Zinssatz()

# Alle Konten anzeigen
print("\nAlle Konten anzeigen:")
Konto.alle_konten()  # Zeigt alle Konten an