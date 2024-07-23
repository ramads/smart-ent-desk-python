from database.core.database import Database
from database.config.config import *

class InsuranceModel:
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
                CREATE TABLE IF NOT EXISTS Asuransi (
                    id_asuransi INT AUTO_INCREMENT PRIMARY KEY,
                    id_pasien INT,
                    nama_asuransi VARCHAR(255) NOT NULL,
                    nomor_asuransi VARCHAR(255) NOT NULL,
                    jenis_asuransi VARCHAR(255),
                    fasilitas_kesehatan VARCHAR(255),
                    kelas_asuransi VARCHAR(255),
                    FOREIGN KEY (id_pasien) REFERENCES Pasien(id_pasien)
                );
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query)
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def insert_insurance(self, patient_id, insurance_name, insurance_number, insurance_type, health_facility, insurance_class):
        try:
            self.open_connection()
            query = """
            INSERT INTO Asuransi (id_pasien, nama_asuransi, nomor_asuransi, jenis_asuransi, fasilitas_kesehatan, kelas_asuransi)
            VALUES (%s, %s, %s, %s, %s, %s);
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query, (patient_id, insurance_name, insurance_number, insurance_type, health_facility, insurance_class))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()


    def get_insurance(self, insurance_id):
        try:
            self.open_connection()
            query = "SELECT * FROM Asuransi WHERE id_asuransi = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (insurance_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    
    def get_all_insurances(self):
        try:
            query = "SELECT * FROM Asuransi"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    
    def get_patient_insurances(self, patient_id):
        try:
            self.open_connection()
            query = "SELECT * FROM Asuransi WHERE id_pasien = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (patient_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
            