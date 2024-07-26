from database.core.database import Database
from database.config.config import *

class NotificationModel:
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
                CREATE TABLE IF NOT EXISTS Notifikasi (
                    id_notifikasi INT AUTO_INCREMENT PRIMARY KEY,
                    notif_header VARCHAR(255) NOT NULL,
                    notif_subheader VARCHAR(255) NOT NULL,
                    notif_content TEXT NOT NULL,
                    notif_datetime DATETIME NOT NULL,
                    already_read BOOLEAN DEFAULT FALSE
                );
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query)
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection

    def insert_notification(self, header, subheader, content, datetime):
        try:
            self.open_connection()
            query = """
            INSERT INTO Notifikasi (notif_header, notif_subheader, notif_content, notif_datetime)
            VALUES (%s, %s, %s, %s);
            """
            cursor = self.db.connection.cursor()
            cursor.execute(query, (header, subheader, content, datetime))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection

    def get_notifications(self):
        try:
            self.open_connection()
            query = "SELECT * FROM Notifikasi"
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    def mark_as_read(self, id_notifikasi):
        try:
            self.open_connection()
            query = "UPDATE Notifikasi SET already_read = TRUE WHERE id_notifikasi = %s"
            cursor = self.db.connection.cursor()
            cursor.execute(query, (id_notifikasi,))
            self.db.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

            