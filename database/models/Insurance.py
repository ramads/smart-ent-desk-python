from database.core.database import Database
from database.config.config import *

class InsuranceModel:
    def __init__(self):
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        self.db.close()

    def insert_insurance(self, id_asuransi, jenis_asuransi, fasilitas_kesehatan):
        try:
            self.open_connection()
            query = """
            INSERT INTO Asuransi (id_asuransi, jenis_asuransi, fasilitas_kesehatan)
            VALUES (%s, %s, %s)
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query, (id_asuransi, jenis_asuransi, fasilitas_kesehatan))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()


    def get_insurance(self, insurance_id):
        try:
            self.open_connection()
            query = "SELECT * FROM Asuransi WHERE id_asuransi = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (insurance_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    
    def get_all_insurances(self):
        try:
            query = "SELECT * FROM Asuransi"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    
    def get_patient_insurances(self, patient_id):
        try:
            self.open_connection()
            query = "SELECT * FROM Asuransi WHERE id_pasien = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (patient_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
            