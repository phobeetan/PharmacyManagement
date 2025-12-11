import sqlite3

class Log:
    def __init__(self, DB_PATH):
        self.DB_PATH = DB_PATH

    def get_connection(self):
        return sqlite3.connect(self.DB_PATH)
    
    def execute(self, sql, params=()): 
        with self.get_connection() as conn:
            conn.execute(sql, params)

    def create_table(self):
        sql =   """
                CREATE TABLE IF NOT EXISTS Log (
                    patientID INTEGER PRIMARY KEY AUTOINCREMENT,
                    firstName TEXT,
                    lastName TEXT
                )
                """
        
        with self.get_connection() as conn:
            conn.execute(sql)

    def insert(self):
        sql =   """
                INSERT INTO Log ()
                VALUES ()
                """
        
        params = ()

        with self.get_connection() as conn:
            conn.execute(sql, params)

    def fetchall(self, sql):
        sql = "SELECT * FROM Log"

        with self.get_connection() as conn:
            cursor = conn.cursor()
            return cursor.execute(sql).fetchall()

    def fetchone(self, column, param=()):
        sql = "SELECT * FROM Log WHERE " + column + " = ?"

        with self.get_connection() as conn:
            cursor = conn.cursor()
            return cursor.execute(sql, param).fetchone()