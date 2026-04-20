import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import Salle


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("500x500")

        self.service = ServiceSalle()

        # Champs de saisie
        self.entry_code = ctk.CTkEntry(self, placeholder_text="Code")
        self.entry_code.pack(pady=5)

        self.entry_libelle = ctk.CTkEntry(self, placeholder_text="Libellé")
        self.entry_libelle.pack(pady=5)

        self.entry_type = ctk.CTkEntry(self, placeholder_text="Type")
        self.entry_type.pack(pady=5)

        self.entry_capacite = ctk.CTkEntry(self, placeholder_text="Capacité")
        self.entry_capacite.pack(pady=5)

        # Boutons
        btn_add = ctk.CTkButton(self, text="Ajouter", command=self.ajouter_salle)
        btn_add.pack(pady=5)

        btn_update = ctk.CTkButton(self, text="Modifier", command=self.modifier_salle)
        btn_update.pack(pady=5)

        btn_delete = ctk.CTkButton(self, text="Supprimer", command=self.supprimer_salle)
        btn_delete.pack(pady=5)

        btn_show = ctk.CTkButton(self, text="Afficher", command=self.afficher_salles)
        btn_show.pack(pady=5)

    # Ajouter
    def ajouter_salle(self):
        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type_salle = self.entry_type.get()
        capacite = int(self.entry_capacite.get())

        s = Salle(code, libelle, type_salle, capacite)
        self.service.ajouter_salle(s)

        print("Salle ajoutée ✔")

    # Modifier
    def modifier_salle(self):
        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type_salle = self.entry_type.get()
        capacite = int(self.entry_capacite.get())

        s = Salle(code, libelle, type_salle, capacite)
        self.service.modifier_salle(s)

        print("Salle modifiée ✔")

    # Supprimer
    def supprimer_salle(self):
        code = self.entry_code.get()
        self.service.supprimer_salle(code)

        print("Salle supprimée ✔")

    # Afficher
    def afficher_salles(self):
        salles = self.service.get_salles()

        for s in salles:
            s.afficher_infos()