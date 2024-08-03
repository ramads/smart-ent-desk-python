from database.core.database import Database
from database.config.config import *

class PatientModel:
    def __init__(self):
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        self.db.close()

    def get_id_desa(self, nama_desa):
        try:
            self.open_connection()
            query = "SELECT id_desa FROM Desa WHERE nama_desa = %s"
            cursor = self.db.connection.cursor()
            cursor.execute(query, (nama_desa,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def insert_patient(self, NIK, nama_pasien, jenis_kelamin, tanggal_lahir, alamat, nama_desa):
        id_desa = self.get_id_desa(nama_desa)
        try:
            self.open_connection()
            query = """
                INSERT INTO Pasien (NIK, nama_pasien, jenis_kelamin, tanggal_lahir, alamat, id_desa)
                VALUES (%s, %s, %s, %s, %s, %s)   
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query, (NIK, nama_pasien, jenis_kelamin, tanggal_lahir, alamat, id_desa))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_patient(self, patient_id):
        try:
            self.open_connection()
            query = "SELECT * FROM Pasien WHERE id_pasien = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (patient_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    
    def get_all_patients(self):
        try:
            self.open_connection()
            query = "SELECT * FROM Pasien"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
