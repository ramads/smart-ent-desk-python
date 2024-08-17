from database.core.database import Database
from database.config.config import *

class RegencyModel:
    def __init__(self):
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        self.db.close()

    def get_regency(self, id_kabupaten):
        try:
            self.open_connection()
            query = "SELECT * FROM Kabupaten WHERE id_kabupaten = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_kabupaten,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    
    def get_all_Regencies(self):
        try:
            self.open_connection()
            query = "SELECT * FROM Kabupaten"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_regency_id(self, nama_kabupaten):
        try:
            self.open_connection()
            query = "SELECT id_kabupaten FROM Kabupaten WHERE nama_kabupaten = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (nama_kabupaten,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_regency_name(self, id_kabupaten):
        try:
            self.open_connection()
            query = "SELECT nama_kabupaten FROM Kabupaten WHERE id_kabupaten = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_kabupaten,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()