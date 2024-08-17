from database.core.database import Database
from database.config.config import *

class MedicalRecordIndicationModel:
    def __init__(self):
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        self.db.close()

    def insert_medical_record_indication(self, id_rekam_medis, id_gejala):
        try:
            self.open_connection()
            query = """
            INSERT INTO Rekam_Medis_Gejala (id_rekam_medis, id_gejala)
            VALUES (%s, %s)
            """
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_rekam_medis, id_gejala))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_all_medical_record_indication(self):
        try:
            self.open_connection()
            query = "SELECT * FROM Rekam_Medis_Gejala"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_medical_record_indication_by_id(self, id_rekam_medis, id_gejala):
        try:
            self.open_connection()
            query = "SELECT * FROM Rekam_Medis_Gejala WHERE id_rekam_medis = %s AND id_gejala = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_rekam_medis, id_gejala,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def delete_medical_record_indication_by_medical_record(self, id_rekam_medis):
        try:
            self.open_connection()
            query = "DELETE FROM Rekam_Medis_Gejala WHERE id_rekam_medis = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_rekam_medis,))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()


            
