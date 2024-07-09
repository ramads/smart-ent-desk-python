from database.core.database import Database
from database.config.config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

class DiagnosisModel:
    def __init__(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)
        self.db.connect()

    def create_table(self):
        query = """
            CREATE TABLE Diagnosa (
                id_diagnosa INT AUTO_INCREMENT PRIMARY KEY,
                id_riwayat INT,
                diagnosa VARCHAR(255) NOT NULL,
                tanggal_diagnosa DATE NOT NULL,
                hasil_diagnosa TEXT,
                tingkat_keparahan INT,
                gambar_diagnosa VARCHAR(255),
                FOREIGN KEY (id_riwayat) REFERENCES Riwayat_Pemeriksaan(id_riwayat)
            );
        """
        cursor = self.db.connection.cursor()
        cursor.execute(query)
        self.db.connection.commit()

    def insert_diagnosis(self, history_id, diagnosis, diagnosis_date, result, severity, image_path):
        query = """
        INSERT INTO diagnoses (id_riwayat, diagnosa, tanggal_diagnosa, hasil_diagnosa, tingkat_keparahan, gambar_diagnosa)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        cursor = self.db.connection.cursor()
        cursor.execute(query, (history_id, diagnosis, diagnosis_date, result, severity, image_path))
        self.db.connection.commit()

    def get_diagnosis(self, diagnosis_id):
        query = "SELECT * FROM Diagnosa WHERE id_riwayat = %s"
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query, (diagnosis_id,))
        return cursor.fetchone()
    
    def get_all_diagnoses(self):
        query = "SELECT * FROM Diagnosa"
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()
    
    def get_history_diagnoses(self, history_id):
        query = "SELECT * FROM Diagnosa WHERE id_riwayat = %s"
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query, (history_id,))
        return cursor.fetchone()
