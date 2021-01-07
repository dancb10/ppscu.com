from pprint import pprint
lista_obiecte=[]

class Catalog(object):
    clasa=[]
    subclasa=[]

    def __init__(self,pret=0,consum=100,producator='Samsung',cod_produs='XXXX'):
        global lista_obiecte
        self.pret=pret
        self.consum=consum
        self.producator=producator
        self.cod_produs=cod_produs
        lista_obiecte.append(self)

    def sort_pret(self):
        sorted_pret = sorted(lista_obiecte, key=lambda obj: obj.pret)
        for obj in sorted_pret:
            print("Pret "+str(obj.pret),"Produs: "+str(obj.cod_produs))

    def sort_consum(self):
        sorted_consum = sorted(lista_obiecte, key=lambda obj: obj.consum)
        for obj in sorted_consum:
            print("Consum: "+str(obj.consum), "Produs: "+str(obj.cod_produs))

    def afiseaza_producator(self, producator):
        mydict = {}
        for obj in lista_obiecte:
            if obj.producator == producator:
                mydict["Produs: "+str(obj.cod_produs)] = obj.__dict__
        pprint(mydict)

class Electrocasnice_mari(Catalog):
    def __init__(self, *args, **kwargs):
        # Catalog.__init__(self, *args, **kwargs)
        super(Electrocasnice_mari, self).__init__(*args, **kwargs)
        print("Obiectul din Electrocasnice_mari: "+self.cod_produs)
        self.adincime = raw_input("Adauga adancime: ")
        self.latime = raw_input("Adauga latime: ")
        self.inaltime = raw_input("Inaltime: ")

class Electrocasnice_mici(Catalog):
    def __init__(self, *args, **kwargs):
        Catalog.__init__(self, *args, **kwargs)
        print("Obiectul din Electrocasnice_mici: " + self.cod_produs)
        self.lungime_cablu = raw_input("Adauga lungime_cablu: ")
        self.baterie = raw_input("Adauga baterie: ")

class Frigider(Electrocasnice_mari):
    def __init__(self, *args, **kwargs):
        Electrocasnice_mari.__init__(self, *args, **kwargs)
        print("Obiectul Frigider din Electrocasnice_mari: "+self.cod_produs)
        self.capacitate_congelator = raw_input("Adauga capacitate congelator: ")
        self.capacitate_frigier = raw_input("Adauga capacitate frigier: ")
        Catalog.clasa.append("Electrocasnice mari")
        Catalog.subclasa.append("Frigider")

class Aragaz(Electrocasnice_mari):
    def __init__(self, *args, **kwargs):
        Electrocasnice_mari.__init__(self, *args, **kwargs)
        print("Obiectul Aragaz din Electrocasnice_mari: "+self.cod_produs)
        self.nr_arzatoare = raw_input("Adauga numar arzatoare: ")
        Catalog.clasa.append("Electrocasnice mari")
        Catalog.subclasa.append("Aragaz")

class Mixer(Electrocasnice_mici):
    def __init__(self, *args, **kwargs):
        Electrocasnice_mici.__init__(self, *args, **kwargs)
        print("Obiectul Mixer din Electrocasnice_mici: "+self.cod_produs)
        self.rotatii_min = raw_input("Adauga nr de rotatii_min: ")
        Catalog.clasa.append("Electrocasnice mici")
        Catalog.subclasa.append("Mixer")

class Fier_calcat(Electrocasnice_mici):
    def __init__(self, *args, **kwargs):
        Electrocasnice_mici.__init__(self, *args, **kwargs)
        print("Obiectul Fier calcat din Electrocasnice_mici: "+self.cod_produs)
        self.rezervor = raw_input("Adauga rezervor: ")
        Catalog.clasa.append("Electrocasnice mici")
        Catalog.subclasa.append("Fier calcat")

frigider1=Frigider(pret=60,consum=120,producator="Samsung",cod_produs="1234")
frigider2=Frigider(pret=15,consum=100,producator="Benq",cod_produs="3598")
aragaz1=Aragaz(pret=5,consum=220,producator="Samsung",cod_produs="4228")
aragaz2=Aragaz(pret=50,consum=180,producator="Noc",cod_produs="2355")
mixer1=Mixer(pret=25,consum=170,producator="Dell",cod_produs="4335")
mixer2=Mixer(pret=10,consum=160,producator="Benq",cod_produs="7734")
fier_calcat1=Fier_calcat(pret=80,consum=110,producator="Benq",cod_produs="2343")
fier_calcat2=Fier_calcat(pret=60,consum=110,producator="Dell",cod_produs="1231")
print("##########################################################")
print("Sortarea obiectelor dupa pret:")
fier_calcat2.sort_pret()
print("##########################################################")
print("Sortarea obiectelor dupa consum:")
fier_calcat2.sort_consum()
print("##########################################################")
print("Sortarea obiectelor dupa producator:")
fier_calcat2.afiseaza_producator("Samsung")
