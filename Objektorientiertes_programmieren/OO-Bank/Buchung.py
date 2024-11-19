class Buchung:
    def __init__(self, betrag, datum, verwendungszweck, empfänger_Konto=None):
        self.betrag = betrag
        self.datum = datum
        self.verwendungszweck = verwendungszweck
        self.empfänger_Konto = empfänger_Konto