from Main import Bank, Jugendkonto, Privatkonto, Sparkonto

from datetime import datetime

# Angenommen, die Bank- und Kontoklassen aus deinem ersten Programm sind hier importiert.

# Konto eröffnen
def konto_eröffnen(bank):
    print("Konto eröffnen:")
    vorname = input("Vorname: ")
    nachname = input("Nachname: ")
    geburtsdatum = input("Geburtsdatum (DD.MM.YYYY): ")
    kontotyp = input("Kontotyp (Privatkonto, Jugendkonto, Sparkonto): ")

    if kontotyp == "Privatkonto":
        konto = bank.Konto_eröffnen(Privatkonto, vorname, nachname, geburtsdatum)
    elif kontotyp == "Jugendkonto":
        konto = bank.Konto_eröffnen(Jugendkonto, vorname, nachname, geburtsdatum)
    elif kontotyp == "Sparkonto":
        konto = bank.Konto_eröffnen(Sparkonto, vorname, nachname, geburtsdatum)
    else:
        print("Unbekannter Kontotyp.")
        return

    print(f"Konto mit der Nummer {konto.get_Konto_ID()} erfolgreich eröffnet!")

# Bareinzahlung auf ein Konto
def bareinzahlung(bank):
    print("Bareinzahlung:")
    konto_id = int(input("Kontonummer: "))
    betrag = float(input("Einzahlungsbetrag: "))
    try:
        konto = bank.get_konto_info(konto_id)
        konto.Bareinzahlung(betrag)
        print(f"{betrag} auf Konto {konto_id} eingezahlt.")
    except ValueError as e:
        print(f"Fehler: {e}")

# Buchung von einem Konto zu einem anderen
def buchung(bank):
    print("Buchung:")
    start_konto_id = int(input("Start-Kontonummer: "))
    ziel_konto_id = int(input("Ziel-Kontonummer: "))
    betrag = float(input("Betrag: "))
    zweck = input("Verwendungszweck (optional): ")
    try:
        bank.Buchung(start_konto_id, ziel_konto_id, betrag, zweck)
        print("Buchung erfolgreich!")
    except ValueError as e:
        print(f"Fehler: {e}")

# Kontostand abfragen
def kontostand_abfragen(bank):
    print("Kontostand abfragen:")
    konto_id = int(input("Kontonummer: "))
    try:
        konto = bank.get_konto_info(konto_id)
        print(f"Kontostand: {konto.get_saldo()} EUR")
    except ValueError as e:
        print(f"Fehler: {e}")

# Letzte Buchungen eines Kontos abfragen
def buchungsjournal_abfragen(bank):
    print("Buchungsjournal abfragen:")
    konto_id = int(input("Kontonummer: "))
    max_einträge = input("Maximale Einträge (optional): ")
    max_einträge = int(max_einträge) if max_einträge else None
    try:
        konto = bank.get_konto_info(konto_id)
        journal = konto.get_journal(max_einträge)
        for eintrag in journal:
            print(eintrag)
    except ValueError as e:
        print(f"Fehler: {e}")

# Letzte Buchungen der Bank abfragen
def bankjournal_abfragen(bank):
    print("Bankjournal abfragen:")
    max_einträge = input("Maximale Einträge (optional): ")
    max_einträge = int(max_einträge) if max_einträge else None
    journal = bank.get_Bankjournal(max_einträge)
    for eintrag in journal:
        print(eintrag)

# Konto schließen
def konto_schliessen(bank):
    print("Konto schließen:")
    konto_id = int(input("Kontonummer: "))
    try:
        if bank.Konto_schliessen(konto_id):
            print(f"Konto {konto_id} wurde erfolgreich geschlossen.")
        else:
            print(f"Konto {konto_id} konnte nicht geschlossen werden.")
    except ValueError as e:
        print(f"Fehler: {e}")

# Hauptmenü
def menu(bank):
    while True:
        print("\n--- Bank Menü ---")
        print("1. Konto eröffnen")
        print("2. Bareinzahlung auf ein Konto")
        print("3. Buchung von einem Konto zu einem anderen")
        print("4. Kontostand abfragen")
        print("5. Letzte Buchungen eines Kontos abfragen")
        print("6. Letzte Buchungen der Bank abfragen")
        print("7. Konto schließen")
        print("8. Beenden")

        auswahl = input("Wählen Sie eine Option: ")

        if auswahl == "1":
            konto_eröffnen(bank)
        elif auswahl == "2":
            bareinzahlung(bank)
        elif auswahl == "3":
            buchung(bank)
        elif auswahl == "4":
            kontostand_abfragen(bank)
        elif auswahl == "5":
            buchungsjournal_abfragen(bank)
        elif auswahl == "6":
            bankjournal_abfragen(bank)
        elif auswahl == "7":
            konto_schliessen(bank)
        elif auswahl == "8":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    # Eine Bankinstanz erstellen
    bank = Bank()

    # Benutzeroberfläche starten
    menu(bank)
