class Maja: # Klases definīcijas
    dzivokli = [] # Dzivoklis

    def __init__(self):
        pirmais = Dzivoklis()
        self.dzivokli.append(pirmais)

    def IegutMajasAugstumu(self):
        augstums = 0
        for dzivoklis in self.dzivokli:
            augstums += dzivoklis.IegutAugstumu()
        print(augstums)

class Dzivoklis:
    augstums = 0
    def IegutAugstumu(self):
        return self.augstums

maja = Maja() # Objekta definīcija
maja.dzivokli
dziv = Dzivoklis() 

class Ekrans:
    augstums: int
class Dators:
    ekrans: Ekrans
    def IegutEkranaIzmeru(self):
        return self.ekrans.augstums
