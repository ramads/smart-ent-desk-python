from database.core.database import Database
from database.config.config import *

class DiagnosisModel:
    def __init__(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def create_table(self):
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

    def insert_diagnosis(self, diagnosis, diagnosis_date, result, confidence, image_path, is_corrected, correction_reason, hospital_id, patient_id, diagnosis_type):
        query = """
        INSERT INTO Diagnosa (diagnosa, tanggal_diagnosa, hasil_diagnosa, tingkat_keyakinan, gambar_diagnosa, prediksi_benar, alasan_koreksi, id_rumah_sakit, id_pasien, jenis_diagnosa)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor = self.db.connection.cursor()
        cursor.execute(query, (diagnosis, diagnosis_date, result, confidence, image_path, is_corrected, correction_reason, hospital_id, patient_id, diagnosis_type))
        self.db.connection.commit()

    def get_diagnosis(self, diagnosis_id):
        query = "SELECT * FROM Diagnosa WHERE id_diagnosis = %s"
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query, (diagnosis_id,))
        return cursor.fetchone()
    
    def get_all_diagnoses(self):
        query = "SELECT * FROM Diagnosa"
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()
    
    def get_patient_diagnoses(self, patient_id):
        query = "SELECT * FROM Diagnosa WHERE id_pasien = %s"
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query, (patient_id,))
        return cursor.fetchall()
    
    def get_patient_joint_diagnoses(self):
        query = """
        SELECT * FROM Diagnosa 
        JOIN Pasien ON Diagnosa.id_pasien = Pasien.id_pasien
        ORDER BY Diagnosa.tanggal_diagnosa DESC
        """
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()
