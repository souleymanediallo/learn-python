from Group.chap_4.felins import Felins


class Tigres(Felins):
    def __init__(self, type_felin, vitesse):
        super().__init__(self, type_felin)
        self.vitesse = vitesse
