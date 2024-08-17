from database.core.database import Database
from database.config.config import *

class LocationModel:
    def __init__(self):
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        self.db.close()

    def insert_location(self, tanggal_lokasi, lat, long):
        try:
            self.open_connection()
            query = """
            INSERT INTO Lokasi (tanggal_lokasi, lat, long)
            VALUES (%s, %s, %s)
            """
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (tanggal_lokasi, lat, long))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
            
    def get_location(self, tanggal_lokasi):
        try:
            self.open_connection()
            query = "SELECT * FROM Lokasi WHERE tanggal_lokasi) = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (tanggal_lokasi,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_all_locations(self):
        try:
            self.open_connection()
            query = "SELECT * FROM Lokasi"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()