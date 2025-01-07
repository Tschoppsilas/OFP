from Main import Bank, Konto, Jugendkonto, Privatkonto, Sparkonto  # Hier importieren wir die Bank und Kontoklassen

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

        option = input("Wählen Sie eine Option: ")

        if option == "1":
            konto_eroeffnen(bank)
        elif option == "2":
            bareinzahlung(bank)
        elif option == "3":
            buchung(bank)
        elif option == "4":
            kontostand_abfragen(bank)
        elif option == "5":
            letzte_buchungen_konto_abfragen(bank)
        elif option == "6":
            letzte_buchungen_bank_abfragen(bank)
        elif option == "7":
            konto_schliessen(bank)
        elif option == "8":
            break
        else:
            print("Ungültige Auswahl. Bitte erneut versuchen.")

def konto_eroeffnen(bank):
    print("\nKonto eröffnen:")
    vorname = input("Vorname: ")
    nachname = input("Nachname: ")
    geburtsdatum = input("Geburtsdatum (DD.MM.YYYY): ")
    kontotyp = input("Kontotyp (Privatkonto, Jugendkonto, Sparkonto): ")

    if kontotyp == "Jugendkonto":
        konto = bank.Konto_eröffnen(Jugendkonto, vorname, nachname, geburtsdatum)
    elif kontotyp == "Privatkonto":
        konto = bank.Konto_eröffnen(Privatkonto, vorname, nachname, geburtsdatum)
    elif kontotyp == "Sparkonto":
        konto = bank.Konto_eröffnen(Sparkonto, vorname, nachname, geburtsdatum)
    else:
        print("Ungültiger Kontotyp.")
        return

    print(f"Konto mit der Nummer {konto.get_Konto_ID()} erfolgreich eröffnet!")

def bareinzahlung(bank):
    print("\nBareinzahlung:")
    kontonummer = int(input("Kontonummer: "))
    betrag = float(input("Einzahlungsbetrag: "))
    konto = bank.get_konto_info(kontonummer)
    konto.Bareinzahlung(betrag)
    print(f"{betrag} erfolgreich eingezahlt.")

def buchung(bank):
    print("\nBuchung von einem Konto zu einem anderen:")
    start_konto_id = int(input("Start-Kontonummer: "))
    ziel_konto_id = int(input("Ziel-Kontonummer: "))
    betrag = float(input("Betrag: "))
    zweck = input("Verwendungszweck (optional): ")
    bank.Buchung(start_konto_id, ziel_konto_id, betrag, zweck)
    print(f"Buchung von {betrag} von Konto {start_konto_id} zu Konto {ziel_konto_id} erfolgreich.")

def kontostand_abfragen(bank):
    kontonummer = int(input("\nKontonummer: "))
    konto = bank.get_konto_info(kontonummer)
    print(f"Kontostand: {konto.get_saldo()} EUR")

def letzte_buchungen_konto_abfragen(bank):
    kontonummer = int(input("\nKontonummer: "))
    konto = bank.get_konto_info(kontonummer)
    max_eintraege = input("Maximale Anzahl von Buchungen (optional): ")
    max_eintraege = int(max_eintraege) if max_eintraege else None
    buchungen = konto.get_journal(max_eintraege)
    print("Letzte Buchungen:")
    for buchung in buchungen:
        print(buchung)

def letzte_buchungen_bank_abfragen(bank):
    max_eintraege = input("\nMaximale Anzahl von Buchungen (optional): ")
    max_eintraege = int(max_eintraege) if max_eintraege else None
    buchungen = bank.get_Bankjournal(max_eintraege)
    print("Letzte Buchungen der Bank:")
    for buchung in buchungen:
        print(buchung)

def konto_schliessen(bank):
    kontonummer = int(input("\nKontonummer zum Schließen: "))
    if bank.Konto_schliessen(kontonummer):
        print(f"Konto {kontonummer} erfolgreich geschlossen.")
    else:
        print("Fehler beim Schließen des Kontos.")


if __name__ == "__main__":
    # Erstelle die Bankinstanz
    bank = Bank()

    # Starte das Menü
    menu(bank)
