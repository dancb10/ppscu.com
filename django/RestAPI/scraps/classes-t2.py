class Operatie(object):

    def __init__(self,a=1,b=2,c=3,d=4):
        try:
            if int(a) and int(b) and int(c) and int(d):
                self.a = a
                self.b = b
                self.c = c
                self.d = d
        except(Exception):
            print("Dati va rog 4 numere")

    def __str__(self):
        try:
            op = ((self.a * (self.b + 3) / self.c) * self.d)
            if op:
                return("Result is: {0}".format(str(op)))
        except(Exception):
            return("error")



a = Operatie(a=5,b=7,c=2,d=2)
print(a)
