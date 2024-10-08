import json
import os
from datetime import datetime, date

from database.core.database import Database
from database.config.config import *
from collections import defaultdict

from pprint import pprint

class DataSync:
    def __init__(self):
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        if self.db:
            self.db.close()

    def save_json_data(self, data):
        current_date = datetime.now().strftime("%Y-%m-%d")
        JSON_DIR = os.path.join("database","data_sync")
        if not os.path.exists(JSON_DIR):
            os.makedirs(JSON_DIR)

        file_path = os.path.join(JSON_DIR, f"{current_date}.json")
        
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        existing_ids = {(record["id_rekam_medis"], record["NIK"]) for record in existing_data}
        new_data = [record for record in data if (record["id_rekam_medis"], record["NIK"]) not in existing_ids]

        combined_data = existing_data + new_data

        with open(file_path, "w") as file:
            json.dump(combined_data, file, indent=4)

    def fetch_mysql_data(self, query):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def sync_data(self):
        try:
            self.open_connection()
            query = """
                SELECT 
                    rm.*, 
                    p.*, 
                    py.nama_penyakit AS nama_penyakit,
                    py.organ_penyakit AS organ_penyakit,
                    rmg.id_rekam_medis AS rmg_id_rekam_medis, 
                    g.id_gejala AS id_gejala, 
                    g.nama_gejala AS nama_gejala
                FROM 
                    Rekam_Medis rm
                JOIN
                    Penyakit py ON rm.id_penyakit = py.id_penyakit
                JOIN 
                    Pasien p ON rm.NIK = p.NIK
                LEFT JOIN 
                    Rekam_Medis_Gejala rmg ON rm.id_rekam_medis = rmg.id_rekam_medis
                LEFT JOIN 
                    Gejala g ON rmg.id_gejala = g.id_gejala
                WHERE 
                    rm.tanggal_pemeriksaan >= NOW() - INTERVAL 1 HOUR
            """
            mysql_data = self.fetch_mysql_data(query)
            for record in mysql_data:
                for key, value in record.items():
                    if isinstance(value, (datetime, date)):
                        record[key] = value.isoformat()
            
            combined_data = self.combine_records(mysql_data)
            
            self.save_json_data(combined_data)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def combine_records(self, data):
        combined_data = defaultdict(lambda: {
            "id_rekam_medis": None,
            "NIK": None,
            "id_penyakit": None,
            "id_faskes": None,
            "tanggal_pemeriksaan": None,
            "tingkat_keyakinan": None,
            "prediksi_benar": None,
            "alasan_koreksi": None,
            "gambar_penyakit": None,
            "deskripsi_gejala": None,
            "nama_pasien": None,
            "tanggal_lahir": None,
            "jenis_kelamin": None,
            "alamat": None,
            "id_desa": None,
            "organ_penyakit": None,
            "gejala": []
        })
        
        for record in data:
            key = (record["id_rekam_medis"], record["NIK"])
            combined_record = combined_data[key]
            
            for field in combined_record:
                if field != "gejala" and combined_record[field] is None:
                    combined_record[field] = record[field]
            
            gejala_info = {
                "id_gejala": record["id_gejala"],
                "nama_gejala": record["nama_gejala"],
            }
            combined_record["gejala"].append(gejala_info)
        
        return list(combined_data.values())