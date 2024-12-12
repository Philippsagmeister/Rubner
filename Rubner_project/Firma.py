class Person:
    def __init__(self, name, geschlecht):
        self.name = name
        self.geschlecht = geschlecht


class Mitarbeiter(Person):
    def __init__(self, name, geschlecht, abteilung=None):
        super().__init__(name, geschlecht)
        self.abteilung = abteilung


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, geschlecht, abteilung=None):
        super().__init__(name, geschlecht, abteilung)


class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []
        self.leiter = None

    def add_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)
        mitarbeiter.abteilung = self

    def set_leiter(self, leiter):
        if not isinstance(leiter, Abteilungsleiter):
            raise ValueError("Leiter muss ein Abteilungsleiter sein!")
        self.leiter = leiter
        self.add_mitarbeiter(leiter)

    def get_anzahl_mitarbeiter(self):
        return len(self.mitarbeiter)

    def get_prozent_frauen_maenner(self):
        frauen = sum(1 for m in self.mitarbeiter if m.geschlecht == "F")
        maenner = sum(1 for m in self.mitarbeiter if m.geschlecht == "M")
        gesamt = frauen + maenner
        return {
            "Frauen": (frauen / gesamt) * 100 if gesamt > 0 else 0,
            "Männer": (maenner / gesamt) * 100 if gesamt > 0 else 0,
        }


class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def add_abteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def anzahl_mitarbeiter(self):
        return sum(abt.get_anzahl_mitarbeiter() for abt in self.abteilungen)

    def anzahl_abteilungsleiter(self):
        return sum(1 for abt in self.abteilungen if abt.leiter is not None)

    def anzahl_abteilungen(self):
        return len(self.abteilungen)

    def groesste_abteilung(self):
        return max(self.abteilungen, key=lambda abt: abt.get_anzahl_mitarbeiter(), default=None)

    def prozent_frauen_maenner(self):
        frauen = sum(sum(1 for m in abt.mitarbeiter if m.geschlecht == "F") for abt in self.abteilungen)
        maenner = sum(sum(1 for m in abt.mitarbeiter if m.geschlecht == "M") for abt in self.abteilungen)
        gesamt = frauen + maenner
        return {
            "Frauen": (frauen / gesamt) * 100 if gesamt > 0 else 0,
            "Männer": (maenner / gesamt) * 100 if gesamt > 0 else 0,
        }


if __name__ == "__main__":
    firma = Firma("Zipfer")

    abt1 = Abteilung("Entwicklung")
    abt2 = Abteilung("Marketing")
    firma.add_abteilung(abt1)
    firma.add_abteilung(abt2)

    leiter1 = Abteilungsleiter("Sebi", "F")
    mitarbeiter1 = Mitarbeiter("Niko", "M")
    mitarbeiter2 = Mitarbeiter("Luggi", "M")

    leiter2 = Abteilungsleiter("Jana", "F")
    mitarbeiter4 = Mitarbeiter("PhilMcChill69", "M")

    abt1.set_leiter(leiter1)
    abt1.add_mitarbeiter(mitarbeiter1)
    abt1.add_mitarbeiter(mitarbeiter2)

    abt2.set_leiter(leiter2)
    abt2.add_mitarbeiter(mitarbeiter4)

    print("Firma:", firma.name)
    print("Anzahl Mitarbeiter:", firma.anzahl_mitarbeiter())
    print("Anzahl Abteilungsleiter:", firma.anzahl_abteilungsleiter())
    print("Anzahl Abteilungen:", firma.anzahl_abteilungen())

    groesste_abt = firma.groesste_abteilung()
    if groesste_abt:
        print(f"Größte Abteilung: {groesste_abt.name} ({groesste_abt.get_anzahl_mitarbeiter()} Mitarbeiter)")

    prozent = firma.prozent_frauen_maenner()
    print(f"Frauenanteil: {prozent['Frauen']}%, Männeranteil: {prozent['Männer']}%")
