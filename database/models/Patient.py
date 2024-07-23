from database.core.database import Database
from database.config.config import *

class PatientModel:
    def __init__(self):
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        self.db.connection.close()

    def create_table(self):
        try:
            self.open_connection()
            query = """
                CREATE TABLE IF NOT EXISTS Pasien (
                    id_pasien INT AUTO_INCREMENT PRIMARY KEY,
                    nama_pasien VARCHAR(255) NOT NULL,
                    jenis_kelamin ENUM('Laki-laki', 'Perempuan') NOT NULL,
                    tanggal_lahir DATE NOT NULL,
                    alamat TEXT
                );
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query)
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection

    def insert_patient(self, name, gender, birth_date, address):
        try:
            self.open_connection()
            query = """
            INSERT INTO Pasien (nama_pasien, jenis_kelamin, tanggal_lahir, alamat)
            VALUES (%s, %s, STR_TO_DATE(%s, '%d %M %Y'), %s);
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query, (name, gender, birth_date, address))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_patient(self, patient_id):
        try:
            self.open_connection()
            query = "SELECT * FROM Pasien WHERE id_pasien = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (patient_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    
    def get_all_patients(self):
        try:
            self.open_connection()
            query = "SELECT * FROM Pasien"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
