from database.core.database import Database
from database.config.config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

class DiagnosisModel:
    def __init__(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS diagnoses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            patient_id INT,
            diagnosis VARCHAR(255) NOT NULL,
            diagnosis_date DATE NOT NULL,
            result TEXT,
            severity INT,
            image_path VARCHAR(255),
            FOREIGN KEY (patient_id) REFERENCES patients(id)
        );
        """
        cursor = self.db.connection.cursor()
        cursor.execute(query)
        self.db.connection.commit()

    def insert_diagnosis(self, patient_id, diagnosis, diagnosis_date, result, severity, image_path):
        query = """
        INSERT INTO diagnoses (patient_id, diagnosis, diagnosis_date, result, severity, image_path)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        cursor = self.db.connection.cursor()
        cursor.execute(query, (patient_id, diagnosis, diagnosis_date, result, severity, image_path))
        self.db.connection.commit()

    def get_diagnosis(self, diagnosis_id):
        query = "SELECT * FROM diagnoses WHERE id = %s"
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query, (diagnosis_id,))
        return cursor.fetchone()
