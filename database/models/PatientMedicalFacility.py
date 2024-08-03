from database.core.database import Database
from database.config.config import *

class PatientMedicalFacilityModel:
    def __init__(self):
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        self.db.close()

    def insert_patient_medical_facility(self, NIK, id_faskes, tanggal_pendaftaran, status_periksa):
        try:
            self.open_connection()
            query = """
            INSERT INTO Pasien_Fasilitas_Kesehatan (NIK, id_faskes, tanggal_pendaftaran, status_periksa)
            VALUES (%s, %s, %s, %s)
            """
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (NIK, id_faskes, tanggal_pendaftaran, status_periksa))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_all_patient_medical_facilities(self):
        try:
            self.open_connection()
            query = "SELECT * FROM Pasien_Fasilitas_Kesehatan"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_queue(self, id_faskes):
        try:
            self.open_connection()
            query = "SELECT * FROM Pasien_Fasilitas_Kesehatan WHERE id_faskes = %s AND status_periksa = 'tunggu' ORDER BY tanggal_pendaftaran ASC"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_faskes,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def update_queue(self, NIK, id_faskes, tanggal_pendaftaran):
        try:
            self.open_connection()
            query = "UPDATE Pasien_Fasilitas_Kesehatan SET status_periksa = 'selesai' WHERE NIK = %s AND id_faskes = %s AND tanggal_pendaftaran = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (NIK, id_faskes, tanggal_pendaftaran))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()