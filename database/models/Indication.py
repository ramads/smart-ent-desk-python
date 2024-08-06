from database.core.database import Database
from database.config.config import *

class IndicationModel:
    def __init__(self):
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        self.db.close()

    def insert_indication(self, nama_gejala, organ_gejala):
        try:
            self.open_connection()
            query = """
            INSERT INTO Gejala (nama_gejala, organ_gejala)
            VALUES (%s, %s)
            """
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (nama_gejala, organ_gejala))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
            
    def get_indication(self, id_gejala):
        try:
            self.open_connection()
            query = "SELECT * FROM Gejala WHERE id_gejala = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_gejala,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_all_indications(self):
        try:
            self.open_connection()
            query = "SELECT * FROM Gejala"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_indication_by_organ(self, organ_gejala):
        try:
            self.open_connection()
            query = "SELECT * FROM Gejala WHERE organ_gejala = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (organ_gejala,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    
