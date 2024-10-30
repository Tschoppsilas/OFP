class Tier:
    def geraeusch_machen(self):
        pass

class Hund(Tier):
    def geraeusch_machen(self):
        print("Wuff")

class Katze(Tier):
    def geraeusch_machen(self):
        print("Miau")

def tier_geraeusch(tier):
    tier.geraeusch_machen()

hund = Hund()
katze = Katze()

tier_geraeusch(hund)  # Ausgabe: Wuff
tier_geraeusch(katze)  # Ausgabe: Miau
