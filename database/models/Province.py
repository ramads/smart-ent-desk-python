from database.core.database import Database
from database.config.config import *

class ProvinceModel:
    def __init__(self):
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        self.db.close()

    def get_province(self, id_provinsi):
        try:
            self.open_connection()
            query = "SELECT * FROM Provinsi WHERE id_provinsi = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_provinsi,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    
    def get_all_provinces(self):
        try:
            self.open_connection()
            query = "SELECT * FROM Provinsi"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_province_id(self, nama_provinsi):
        try:
            self.open_connection()
            query = "SELECT id_provinsi FROM Provinsi WHERE nama_provinsi = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (nama_provinsi,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_province_name(self, id_provinsi):
        try:
            self.open_connection()
            query = "SELECT nama_provinsi FROM Provinsi WHERE id_provinsi = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_provinsi,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()