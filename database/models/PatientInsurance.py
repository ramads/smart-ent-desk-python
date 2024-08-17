from database.core.database import Database
from database.config.config import *

class PatientInsuranceModel:
    def __init__(self):
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        self.db.close()

    def insert_patient_insurance(self, NIK, id_asuransi, tanggal_klaim, nomor_asuransi, kelas_asuransi):
        try:
            self.open_connection()
            query = """
            INSERT INTO Pasien_Asuransi (NIK, id_asuransi, tanggal_klaim, nomor_asuransi, kelas_asuransi)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query, (NIK, id_asuransi, tanggal_klaim, nomor_asuransi, kelas_asuransi))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_patient_insurance(self, NIK):
        try:
            self.open_connection()
            query = "SELECT * FROM Pasien_Asuransi WHERE NIK = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (NIK,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
