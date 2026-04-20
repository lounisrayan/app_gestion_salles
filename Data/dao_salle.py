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