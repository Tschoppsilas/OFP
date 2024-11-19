import datetime
import sys
from Test import Konto, Jugendkonto, Sparkonto, Privatkonto
from Bank import Bank
from Buchung import Buchung

# Instanziierung von Objekten
jugendkonto = Jugendkonto()
sparkonto = Sparkonto()

# Bareinzahlung durchführen
print("Bareinzahlung")
sparkonto.bareinzahlung(1000)
sparkonto.abfrage_kontostand()

# Kontoübertrag durchführen
sparkonto.Kontoübertrag(200, 1, "Testüberweisung")

# Abfrage des Kontostands des Gebührenkontos (Kontonummer 0)
print(Konto.konten[0]['Saldo'])  # Gebührenkonto

# Buchungsabfrage
sparkonto.Buchungsabfrage(1)  # Abfrage der letzten Buchung auf Sparkonto

# Alle Konten anzeigen
Konto.alle_konten()  # Zeigt alle Konten an