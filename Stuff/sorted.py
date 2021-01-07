class prajituri(object):
    list=[]
    def __init__(self,nume,pret):
        self.nume = nume
        self.pret = pret
        prajituri.list.append(self)

    def sorteaza_dupa_pret(self):
        for obj in sorted(prajituri.list,key=lambda obiect: obiect.pret):
            print("========")
            print('Nume',obj.nume)
            print("Pret",obj.pret)

o1 = prajituri("Savarina",10)
o2 = prajituri("Ecler",40)
o3 = prajituri("Amandina",5)
o4 = prajituri("Macaroons",20)
o4.sorteaza_dupa_pret()
