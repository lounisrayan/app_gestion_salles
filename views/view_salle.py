from services.services_salle import ServiceSalle

service = ServiceSalle()

def menu():
    while True:
        print("\n===== MENU SALLE =====")
        print("1. Ajouter salle")
        print("2. Afficher toutes les salles")
        print("3. Quitter")

        choix = input("Choix : ")

        if choix == "1":
            code = input("Code : ")
            libelle = input("Libellé : ")
            type_salle = input("Type : ")
            capacite = int(input("Capacité : "))

            from models.salle import Salle
            s = Salle(code, libelle, type_salle, capacite)

            service.ajouter_salle(s)
            print("Salle ajoutée ✔️")

        elif choix == "2":
            salles = service.get_salles()
            for s in salles:
                s.afficher_infos()

        elif choix == "3":
            break

        else:
            print("Choix invalide")