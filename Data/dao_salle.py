import mysql.connector
import json


class DataSalle:

    def get_connection(self):
        with open("Data/config.json") as f:
            config = json.load(f)

        connection = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )

        return connection

    def insert_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
        values = (salle.code, salle.libelle, salle.type, salle.capacite)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

    def update_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "UPDATE salle SET libelle=%s, type=%s, capacite=%s WHERE code=%s"
        values = (salle.libelle, salle.type, salle.capacite, salle.code)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

    def delete_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM salle WHERE code=%s"
        values = (code,)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

    def get_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM salle WHERE code=%s"
        values = (code,)

        cursor.execute(query, values)
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result:
            from models.salle import Salle
            return Salle(result[0], result[1], result[2], result[3])
        else:
            return None