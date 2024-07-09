from database.core.database import Database
from database.config.config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

class PatientModel:
    def __init__(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)
        self.db.connect()

    def create_table(self):
        query = """
            CREATE TABLE Pasien (
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

    def insert_patient(self, name, gender, birth_date, address):
        query = """
        INSERT INTO Pasien (nama_pasien, jenis_kelamin, tanggal_lahir, alamat)
        VALUES (%s, %s, STR_TO_DATE(%s, '%d %M %Y'), %s);
        """
        cursor = self.db.connection.cursor()
        cursor.execute(query, (name, gender, birth_date, address))
        self.db.connection.commit()

    def get_patient(self, patient_id):
        query = "SELECT * FROM Pasien WHERE id = %s"
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query, (patient_id))
        return cursor.fetchone()
    
    def get_all_patients(self):
        query = "SELECT * FROM Pasien"
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()
