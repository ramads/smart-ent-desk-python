from database.core.database import Database
from database.config.config import *

class DiseaseModel:
    def __init__(self):
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        self.db.close()

    def get_insert(self, nama_penyakit, deskripsi_penyakit, organ_penyakit):
        try:
            self.open_connection()
            query = """
            INSERT INTO penyakit (nama_penyakit, deskripsi_penyakit, organ_penyakit)
            VALUES (%s, %s, %s)
            """
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (nama_penyakit, deskripsi_penyakit, organ_penyakit))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_disease(self, id_penyakit):
        try:
            self.open_connection()
            query = "SELECT * FROM Penyakit WHERE id_penyakit = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_penyakit,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_all_diseases(self):
        try:
            self.open_connection()
            query = "SELECT * FROM Penyakit"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_all_diseases_by_diagnosis_type(self, diagnosis_type):
        print(diagnosis_type)
        try:
            self.open_connection()
            query = "SELECT * FROM Penyakit WHERE organ_penyakit = %s ORDER BY Penyakit.nama_penyakit"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (diagnosis_type,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_disease_id(self, nama_penyakit):
        try:
            self.open_connection()
            query = "SELECT id_penyakit FROM Penyakit WHERE nama_penyakit = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (nama_penyakit,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    