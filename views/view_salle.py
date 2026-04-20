# Interface utilisateur gestion des salles
from services.services_salle import ServiceSalle

service = ServiceSalle()

def menu():
    while True:
        print("Bienvenue dans l'application de gestion des salles")
        print("==== GESTION DES SALLES ====")
        print("\n===== MENU SALLE =====")
        print("1. Ajouter une salle")
        print("2. Afficher toutes les salles")
        print("3. Quitter le programme")
        print("4. Supprimer salle")
        print("5. Modifier salle")

        choix = input("Choix : ")

        if choix == "1":
            code = input("Code : ")
            libelle = input("Libellé : ")
            type_salle = input("Type : ")
            capacite = int(input("Capacité : "))

            from models.salle import Salle
            s = Salle(code, libelle, type_salle, capacite)

            service.ajouter_salle(s)
            print("Salle ajoutée ✔")

        elif choix == "2":
            salles = service.get_salles()
            for s in salles:
                s.afficher_infos()
        elif choix == "4":
            code = input("Code à supprimer : ")
            service.supprimer_salle(code)
            print("Salle supprimée ✔")
        elif choix == "5":
            code = input("Code : ")
            libelle = input("Nouveau libellé : ")
            type_salle = input("Nouveau type : ")
            capacite = int(input("Nouvelle capacité : "))

            from models.salle import Salle
            s = Salle(code, libelle, type_salle, capacite)

            service.modifier_salle(s)
            print("Salle modifiée ✔")


        elif choix == "3":
            print("Au revoir ")
            break

        else:
            print("Choix invalide")