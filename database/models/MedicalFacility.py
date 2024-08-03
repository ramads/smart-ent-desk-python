from database.core.database import Database
from database.config.config import *

class MedicalFacilityModel:
    def __init__(self):
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        self.db.close()

    def insert_medical_facilitiy(self, nama_faskes, alamat_faskes, jumlah_tenaga_ahli, jumlah_award, jumlah_partner, no_hp_faskes, email_faskes):
        try:
            self.open_connection()
            query = """
            INSERT INTO Faskes (nama_faskes, alamat_faskes, jumlah_tenaga_ahli, jumlah_award, jumlah_partner, no_hp_faskes, email_faskes)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query, (nama_faskes, alamat_faskes, jumlah_tenaga_ahli, jumlah_award, jumlah_partner, no_hp_faskes, email_faskes))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_medical_facility(self, medical_facility_id):
        try:
            self.open_connection()
            query = "SELECT * FROM Faskes WHERE id_faskes = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (medical_facility_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_all_medical_facilities(self):
        try:
            self.open_connection()
            query = "SELECT * FROM Faskes"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    
    
