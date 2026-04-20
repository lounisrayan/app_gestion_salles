import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import Salle
from tkinter import ttk


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("500x500")

        self.service = ServiceSalle()


        self.entry_code = ctk.CTkEntry(self, placeholder_text="Code")
        self.entry_code.pack(pady=5)

        self.entry_libelle = ctk.CTkEntry(self, placeholder_text="Libellé")
        self.entry_libelle.pack(pady=5)

        self.entry_type = ctk.CTkEntry(self, placeholder_text="Type")
        self.entry_type.pack(pady=5)

        self.entry_capacite = ctk.CTkEntry(self, placeholder_text="Capacité")
        self.entry_capacite.pack(pady=5)


        btn_add = ctk.CTkButton(self, text="Ajouter", command=self.ajouter_salle)
        btn_add.pack(pady=5)

        btn_update = ctk.CTkButton(self, text="Modifier", command=self.modifier_salle)
        btn_update.pack(pady=5)

        btn_delete = ctk.CTkButton(self, text="Supprimer", command=self.supprimer_salle)
        btn_delete.pack(pady=5)

        btn_show = ctk.CTkButton(self, text="Afficher", command=self.charger_salles)
        btn_show.pack(pady=5)


        self.tree = ttk.Treeview(self, columns=("code", "libelle", "type", "capacite"), show="headings")

        self.tree.heading("code", text="Code")
        self.tree.heading("libelle", text="Libellé")
        self.tree.heading("type", text="Type")
        self.tree.heading("capacite", text="Capacité")

        self.tree.pack(pady=10)


        self.charger_salles()


    def charger_salles(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        salles = self.service.get_salles()

        for s in salles:
            self.tree.insert("", "end", values=(s.code, s.libelle, s.type, s.capacite))


    def ajouter_salle(self):
        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type_salle = self.entry_type.get()
        capacite = int(self.entry_capacite.get())

        s = Salle(code, libelle, type_salle, capacite)
        self.service.ajouter_salle(s)

        self.charger_salles()

        print("Salle ajoutée ✔")


    def modifier_salle(self):
        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type_salle = self.entry_type.get()
        capacite = int(self.entry_capacite.get())

        s = Salle(code, libelle, type_salle, capacite)
        self.service.modifier_salle(s)

        self.charger_salles()

        print("Salle modifiée ✔")


    def supprimer_salle(self):
        code = self.entry_code.get()
        self.service.supprimer_salle(code)

        self.charger_salles()

        print("Salle supprimée ✔")