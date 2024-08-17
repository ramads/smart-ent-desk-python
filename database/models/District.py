from database.core.database import Database
from database.config.config import *

class DistrictModel:
    def __init__(self):
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        self.db.close()

    def get_district(self, id_kecamatan):
        try:
            self.open_connection()
            query = "SELECT * Kecamatan WHERE id_kecamatan = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_kecamatan,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    
    def get_all_Regencies(self):
        try:
            self.open_connection()
            query = "SELECT * Kecamatan"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_district_id(self, nama_kecamatan):
        try:
            self.open_connection()
            query = "SELECT id_kecamatan Kecamatan WHERE nama_kecamatan = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (nama_kecamatan,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_district_name(self, id_kecamatan):
        try:
            self.open_connection()
            query = "SELECT nama_kecamatan FROM Kecamatan WHERE id_kecamatan = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_kecamatan,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()