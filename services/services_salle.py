from Data.dao_salle import DataSalle

class ServiceSalle:

    def __init__(self):
        self.dao = DataSalle()

    def ajouter_salle(self, salle):
        self.dao.insert_salle(salle)

    def modifier_salle(self, salle):
        self.dao.update_salle(salle)

    def supprimer_salle(self, code):
        self.dao.delete_salle(code)

    def get_salle(self, code):
        return self.dao.get_salle(code)

    def get_salles(self):
        return self.dao.get_salles()