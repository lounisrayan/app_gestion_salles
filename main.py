from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

# test insertion
s = Salle("A1", "Salle Test", "Classe", 30)
dao.insert_salle(s)

# test récupération
result = dao.get_salle("A1")

if result:
    result.afficher_infos()
else:
    print("Salle non trouvée")