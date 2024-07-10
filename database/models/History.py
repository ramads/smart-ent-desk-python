from database.core.database import Database
from database.config.config import *

class HistoryModel:
    def __init__(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS Riwayat_Pemeriksaan (
                id_riwayat INT AUTO_INCREMENT PRIMARY KEY,
                id_pasien INT,
                id_rumah_sakit INT,
                organ ENUM('Telinga', 'Hidung', 'Tenggorokan') NOT NULL,
                FOREIGN KEY (id_rumah_sakit) REFERENCES Rumah_Sakit(id_rumah_sakit),
                FOREIGN KEY (id_pasien) REFERENCES Pasien(id_pasien)
            );
        """
        cursor = self.db.connection.cursor()
        cursor.execute(query)
        self.db.connection.commit()

    def insert_history(self, patient_id, hospital_id, organ):
        query = """
        INSERT INTO Riwayat_Pemeriksaan (id_pasien, id_rumah_sakit, organ)
        VALUES (%s, %s, %s);
        """
        cursor = self.db.connection.cursor()
        cursor.execute(query, (patient_id, hospital_id, organ,))
        history_id = cursor.lastrowid
        self.db.connection.commit()
        return history_id

    def get_history(self, history_id):
        query = "SELECT * FROM Riwayat_Pemeriksaan WHERE id_riwayat = %s"
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query, (history_id,))
        return cursor.fetchone()
    
    def get_all_histories(self):
        query = "SELECT * FROM Riwayat_Pemeriksaan"
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()
    
    def get_patient_histories_join_diagnosis(self, patient_id):
        query = """
        SELECT * FROM Riwayat_Pemeriksaan
        JOIN Diagnosa
        ON Riwayat_Pemeriksaan.id_riwayat = Diagnosa.id_riwayat
        WHERE Riwayat_Pemeriksaan.id_pasien = %s
        ORDER BY Diagnosa.tanggal_diagnosa DESC
        """
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query, (patient_id,))
        return cursor.fetchall()