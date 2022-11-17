from multipul_Inharitance1.Father import Father
from multipul_Inharitance1.Father1 import Parent1


class Childs(Father,Parent1):
    def __init__(self,money,bike,bus,forms,yields,properies):
        Father.__init__(self, money, bike, bus)
        Parent1.__init__(forms)
        self.yields = yields
        self.propertis = properies

    def get_yields(self):
        return self.yields

    def display_properties(self):
        print(self.propertis)
