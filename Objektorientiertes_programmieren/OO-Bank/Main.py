import datetime
import sys
from Test import Konto, Jugendkonto, Sparkonto, Privatkonto
from Bank import Bank
from Buchung import Buchung

# Instanziierung von Objekten
privatkonto = Privatkonto()
Jugendkonto = Jugendkonto()
# Bareinzahlung durchführen
print("Bareinzahlung")
privatkonto.bareinzahlung(1000)
Konto.alle_konten()

# Kontoübertrag durchführen
privatkonto.Kontoübertrag(200, 2, "Testüberweisung")

# Abfrage des Kontostands des Gebührenkontos (Kontonummer 0)
print(Konto.konten[0]['Saldo'])  # Gebührenkonto

# Buchungsabfrage
privatkonto.Buchungsabfrage(1)  # Abfrage der letzten Buchung auf Sparkonto

# Alle Konten anzeigen
Konto.alle_konten()  # Zeigt alle Konten an
