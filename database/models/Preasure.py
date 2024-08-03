from database.core.database import Database
from database.config.config import *

class PreasureModel:
    def __init__(self):
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        self.db.close()

    def get_insert(self, level_tekanan, durasi_tekanan, jenis_alat_tekanan, id_rekam_medis):
        try:
            self.open_connection()
            query = """
            INSERT INTO tekanan_darah (level_tekanan, durasi_tekanan, jenis_alat_tekanan, id_rekam_medis)
            VALUES (%s, %s, %s, %s)
            """
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (level_tekanan, durasi_tekanan, jenis_alat_tekanan, id_rekam_medis,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_preasure(self, id_tekanan):
        try:
            self.open_connection()
            query = "SELECT * FROM tekanan_darah WHERE id_tekanan = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_tekanan,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_all_preasures(self):
        try:
            self.open_connection()
            query = "SELECT * FROM tekanan_darah"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_preasure_by_medical_record(self, id_rekam_medis):
        try:
            self.open_connection()
            query = "SELECT * FROM tekanan_darah WHERE id_rekam_medis = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (id_rekam_medis,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

            

