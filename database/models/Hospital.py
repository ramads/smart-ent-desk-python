from database.core.database import Database
from database.config.config import *

class HospitalModel:
    def __init__(self):
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        self.db.close()

    def create_table(self):
        try:
            self.open_connection()
            query = """
                CREATE TABLE IF NOT EXISTS Rumah_Sakit (
                    id_rumah_sakit INT AUTO_INCREMENT PRIMARY KEY,
                    nama_rumah_sakit VARCHAR(255) NOT NULL,
                    alamat_rumah_sakit TEXT NOT NULL,
                    phone_number_rumah_sakit VARCHAR(20),
                    email_rumah_sakit VARCHAR(255),
                    situs_rumah_sakit VARCHAR(255),
                    tentang_rumah_sakit VARCHAR(255),
                    jumlah_partner int,
                    jumlah_award int,
                    jumlah_tenang_ahli int
                );
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query)
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def insert_hospital(self, hospital_name, hospital_address, hospital_phone_number):
        try:
            self.open_connection()
            query = """
            INSERT INTO Rumah_Sakit (nama_rumah_sakit, alamat_rumah_sakit, phone_number_rumah_sakit)
            VALUES (%s, %s, %s);
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query, (hospital_name, hospital_address, hospital_phone_number))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_hospital(self, hospital_id):
        try:
            self.open_connection()
            query = "SELECT * FROM Rumah_Sakit WHERE id_rumah_sakit = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (hospital_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    
    def get_all_hospitals(self):
        try:
            self.open_connection()
            query = "SELECT * FROM Rumah_Sakit"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    
    
