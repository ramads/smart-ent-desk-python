from database.core.database import Database
from database.config.config import *
import uuid

class MedicalRecordModel:
    def __init__(self):
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        self.db.close()

    def insert_medical_record(self, tanggal_pemeriksaan, tingkat_keyakinan, prediksi_benar, alasan_koreksi, gambar_penyakit, NIK, id_faskes, id_penyakit):
        id_rekam_medis = str(uuid.uuid4())
        try:
            self.open_connection()
            query = """
            INSERT INTO Diagnosa (id_rekam_medis, tanggal_pemeriksaan, tingkat_keyakinan, prediksi_benar, alasan_koreksi, gambar_penyakit, NIK, id_faskes, id_penyakit)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query, (id_rekam_medis, tanggal_pemeriksaan, tingkat_keyakinan, prediksi_benar, alasan_koreksi, gambar_penyakit, NIK, id_faskes, id_penyakit))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_medical_record(self, medical_record_id):
        try:
            self.open_connection()
            query = "SELECT * FROM Diagnosa WHERE id_rekam_medis = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (medical_record_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_all_medical_records(self):
        try:
            self.open_connection()
            query = "SELECT * FROM Diagnosa"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    
    def get_patient_medical_record(self, NIK):
        try:
            self.open_connection()
            query = "SELECT * FROM Diagnosa WHERE NIK = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (NIK,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    
    def get_patient_join_diagnoses(self, NIK):
        try:
            self.open_connection()
            query = """
            SELECT * FROM Diagnosa 
            JOIN Pasien ON Diagnosa.NIK = Pasien.NIK
            WHERE Diagnosa.NIK = %s
            ORDER BY Diagnosa.tanggal_pemeriksaan DESC
            """
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (NIK,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def delete_medical_record(self, id_rekam_medis):
        try:
            self.open_connection()
            query = "DELETE FROM Diagnosa WHERE id_rekam_medis = %s"
            cursor = self.db.connection.cursor()
            cursor.execute(query, (id_rekam_medis,))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def update_medical_record(self, id_rekam_medis, tanggal_pemeriksaan, tingkat_keyakinan, prediksi_benar, alasan_koreksi, gambar_penyakit, NIK, id_faskes, id_penyakit):
        try:
            self.open_connection()
            query = """
            UPDATE Diagnosa
            SET tanggal_pemeriksaan = %s, tingkat_keyakinan = %s, prediksi_benar = %s, alasan_koreksi = %s, gambar_penyakit = %s, NIK = %s, id_faskes = %s, id_penyakit = %s
            WHERE id_rekam_medis = %s
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query, (tanggal_pemeriksaan, tingkat_keyakinan, prediksi_benar, alasan_koreksi, gambar_penyakit, NIK, id_faskes, id_penyakit, id_rekam_medis))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
