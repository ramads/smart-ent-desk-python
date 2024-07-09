from database.core.database import Database
from database.config.config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

class HistoryModel:
    def __init__(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)
        self.db.connect()

    def create_table(self):
        query = """
            CREATE TABLE Riwayat_Pemeriksaan (
                id_riwayat INT AUTO_INCREMENT PRIMARY KEY,
                id_pasien INT,
                id_rumah_sakit INT,
                jenis_penyakit VARCHAR(255) NOT NULL,
                tanggal_pemeriksaan DATE NOT NULL,
                keterangan TEXT,
                FOREIGN KEY (id_rumah_sakit) REFERENCES Rumah_Sakit(id_rumah_sakit),
                FOREIGN KEY (id_pasien) REFERENCES Pasien(id_pasien)
            );
        """
        cursor = self.db.connection.cursor()
        cursor.execute(query)
        self.db.connection.commit()

    def insert_history(self, patient_id, hospital_id, kind_of_disease, examination_date, explanation):
        query = """
        INSERT INTO Riwayat_Pemeriksaan (id_pasien, id_rumah_sakit, jenis_penyakit, tanggal_pemeriksaan, keterangan)
        VALUES (%s, STR_TO_DATE(%s, '%d %M %Y'), %s);
        """
        cursor = self.db.connection.cursor()
        cursor.execute(query, (patient_id, hospital_id, kind_of_disease, examination_date, explanation))
        self.db.connection.commit()

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
    
    def get_patient_histories(self, patient_id):
        query = "SELECT * FROM Riwayat_Pemeriksaan WHERE id_pasien = %s order by tanggal_pemeriksaan desc"
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query, (patient_id,))
        return cursor.fetchall()