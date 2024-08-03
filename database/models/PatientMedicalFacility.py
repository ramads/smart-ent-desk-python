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

    def insert_patient_medical_facility(self, id_pasien, id_faskes, tanggal_pendaftaran, status_periksa):
        try:
            self.open_connection()
            query = """
            INSERT INTO pasien_faskes (id_pasien, id_faskes, tanggal_pendaftaran, status_periksa)
            VALUES (%s, %s, %s, %s)
            """
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_pasien, id_faskes, tanggal_pendaftaran, status_periksa))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_all_patient_medical_facilities(self):
        try:
            self.open_connection()
            query = "SELECT * FROM pasien_faskes"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_patient_medical_facility_by_all_id(self, id_pasien, id_faskes, tanggal_pendaftaran):
        try:
            self.open_connection()
            query = "SELECT * FROM pasien_faskes WHERE id_pasien = %s AND id_faskes = %s AND tanggal_pendaftaran = %s ORDER BY tanggal_pendaftaran DESC"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_pasien, id_faskes, tanggal_pendaftaran,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_patient_medical_facility_by_patient(self, id_pasien):
        try:
            self.open_connection()
            query = "SELECT id_pasien_faskes FROM pasien_faskes WHERE id_pasien = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_pasien,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_patient_medical_facility_by_medical_facilitiy(self, id_faskes):
        try:
            self.open_connection()
            query = "SELECT nama_faskes FROM pasien_faskes WHERE id_faskes = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_faskes,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()