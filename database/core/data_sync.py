import json
import os
from datetime import datetime

from database.core.database import Database
from database.config.config import *

class DataSync:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.db = None

    def open_connection(self):
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.db.connect()

    def close_connection(self):
        if self.db:
            self.db.close()

    def load_json_data(self):
        if os.path.exists(self.json_file_path):
            with open(self.json_file_path, 'r') as file:
                return json.load(file)
        return {}

    def save_json_data(self, data):
        with open(self.json_file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def fetch_mysql_data(self, query):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def sync_data(self, table_name):
        try:
            self.open_connection()
            query = f"SELECT * FROM {table_name}"
            mysql_data = self.fetch_mysql_data(query)
            for record in mysql_data:
                for key, value in record.items():
                    if isinstance(value, datetime):
                        record[key] = value.isoformat()
            
            self.save_json_data({table_name: mysql_data})
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()