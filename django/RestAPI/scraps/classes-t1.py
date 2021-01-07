class Catalog(object):

    def __init__(self, nume, prenume, absente=0):
        self.nume = nume
        self.prenume = prenume
        self.absente = absente

    def __str__(self):
        return self.absente

    def incrementeaza_absente(self, value):
        self.absente += int(value)

    def sterge_absente(self, numar=0):
        try:
            x = int(numar)
            if x:
                if self.absente - x  > 0:
                    self.absente -= x
                else:
                    self.absente = 0
        except Exception as e:
            print("Nu ati introdus un numar")

    def printeaza_absente(self):
        print("Studentul " + str(self.nume) + " " + str(self.prenume) + " are " + str(
            self.absente) + " absente")

student1 = Catalog("Ion", "Roata")
student1.printeaza_absente()
student1.incrementeaza_absente(3)
student1.printeaza_absente()
student1.sterge_absente(2)
student1.printeaza_absente()
print("\n")
student2 = Catalog("George","Cerc")
student2.incrementeaza_absente(4)
student2.printeaza_absente()
student2.sterge_absente(2)
student2.printeaza_absente()