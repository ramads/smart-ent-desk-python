from database.core.database import Database
from database.config.config import *

class DiagnosisModel:
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
                CREATE TABLE IF NOT EXISTS Diagnosa (
                    id_diagnosa INT AUTO_INCREMENT PRIMARY KEY,
                    id_pasien INT NOT NULL,
                    id_rumah_sakit INT NOT NULL,
                    jenis_diagnosa ENUM('telinga', 'hidung', 'tenggorokan'),
                    diagnosa VARCHAR(255) NOT NULL,
                    tanggal_diagnosa DATE NOT NULL,
                    hasil_diagnosa TEXT,
                    tingkat_keparahan INT,
                    gambar_diagnosa VARCHAR(255),
                    prediksi_benar BOOLEAN,
                    alasan_koreksi TEXT,
                    FOREIGN KEY (id_riwayat) REFERENCES Riwayat_Pemeriksaan(id_riwayat),
                    FOREIGN KEY (id_rumah_sakit) REFERENCES Rumah_Sakit(id_rumah_sakit),
                    FOREIGN KEY (id_pasien) REFERENCES Pasien(id_pasien)
                );
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query)
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection


    def insert_diagnosis(self, diagnosis, diagnosis_date, result, confidence, image_path, is_corrected, correction_reason, hospital_id, patient_id, diagnosis_type):
        try:
            self.open_connection()
            query = """
            INSERT INTO Diagnosa (diagnosa, tanggal_diagnosa, hasil_diagnosa, tingkat_keyakinan, gambar_diagnosa, prediksi_benar, alasan_koreksi, id_rumah_sakit, id_pasien, jenis_diagnosa)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query, (diagnosis, diagnosis_date, result, confidence, image_path, is_corrected, correction_reason, hospital_id, patient_id, diagnosis_type))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def get_diagnosis(self, diagnosis_id):
        try:
            self.open_connection()
            query = "SELECT * FROM Diagnosa WHERE id_diagnosis = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (diagnosis_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    
    def get_all_diagnoses(self):
        try:
            self.open_connection()
            query = "SELECT * FROM Diagnosa"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    
    def get_patient_diagnoses(self, patient_id):
        try:
            self.open_connection()
            query = "SELECT * FROM Diagnosa WHERE id_pasien = %s"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, (patient_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()
    
    def get_patient_joint_diagnoses(self):
        try:
            self.open_connection()
            query = """
            SELECT * FROM Diagnosa 
            JOIN Pasien ON Diagnosa.id_pasien = Pasien.id_pasien
            ORDER BY Diagnosa.tanggal_diagnosa DESC
            """
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def delete_diagnosis(self, diagnosis_id):
        try:
            self.open_connection()
            query = "DELETE FROM Diagnosa WHERE id_diagnosa = %s"
            cursor = self.db.connection.cursor()
            cursor.execute(query, (diagnosis_id,))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def update_diagnosis(self, id_diagnosis, diagnosis, diagnosis_date, result, confidence, image_path, is_corrected, correction_reason, hospital_id, patient_id, diagnosis_type):
        try:
            self.open_connection()
            query = """
            UPDATE Diagnosa
            SET diagnosa = %s, tanggal_diagnosa = %s, hasil_diagnosa = %s, tingkat_keyakinan = %s, gambar_diagnosa = %s, prediksi_benar = %s, alasan_koreksi = %s, id_rumah_sakit = %s, id_pasien = %s, jenis_diagnosa = %s
            WHERE id_diagnosa = %s
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query, (diagnosis, diagnosis_date, result, confidence, image_path, is_corrected, correction_reason, hospital_id, patient_id, diagnosis_type, id_diagnosis))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()