class Herz:
    def schlaegt(self):
        return "Das Herz schlägt."

class Hund:
    def __init__(self, name, herz):
        self.name = name
        self.herz = herz  # Ein Hund hat ein Herz

    def lebendig(self):
        return f"{self.name} ist lebendig: {self.herz.schlaegt()}"

herz = Herz()
mein_hund = Hund("Bello", herz)
print(mein_hund.lebendig())