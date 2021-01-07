class FabricaDeAnimale:

    def __init__(self):
        pass

    def __call__(self, var=1):
        if var:
            return "cat"
        return "dog"

F = FabricaDeAnimale()
a = F(0)
print(a)
