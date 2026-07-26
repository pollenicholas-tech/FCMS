import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).parent / "fcms.db"

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS main_families(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            family_name TEXT NOT NULL,
            coordinator TEXT,
            description TEXT
        )
        """)
        self.conn.commit()

    def add_main_family(self,family_name,coordinator,description):
        self.cursor.execute(
            "INSERT INTO main_families(family_name,coordinator,description) VALUES(?,?,?)",
            (family_name,coordinator,description))
        self.conn.commit()

    def get_main_families(self):
        self.cursor.execute(
            "SELECT id,family_name,coordinator,description FROM main_families ORDER BY family_name")
        return self.cursor.fetchall()

    def update_main_family(self,family_id,family_name,coordinator,description):
        self.cursor.execute(
            "UPDATE main_families SET family_name=?,coordinator=?,description=? WHERE id=?",
            (family_name,coordinator,description,family_id))
        self.conn.commit()

    def delete_main_family(self,family_id):
        self.cursor.execute("DELETE FROM main_families WHERE id=?",(family_id,))
        self.conn.commit()

    def search_main_families(self,keyword):
        self.cursor.execute(
            "SELECT id,family_name,coordinator,description FROM main_families WHERE family_name LIKE ? OR coordinator LIKE ? ORDER BY family_name",
            (f"%{keyword}%",f"%{keyword}%"))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
