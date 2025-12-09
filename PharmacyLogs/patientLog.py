import sqlite3
import bcrypt
from logSet import Log

class patientLog(Log):
    def __init__(self, DB_PATH):
        self.DB_PATH = DB_PATH
        super().__init__("PharmacyLogs/patientLog.db")

    def get_connection(self):
        return sqlite3.connect(self.DB_PATH)

    def create_table(self):
        sql =   """
                CREATE TABLE IF NOT EXISTS patientLog (
                    patientID integer primary key,
                    firstName text,
                    lastName text,
                    birthday text,
                    email UNIQUE text,
                    password text
                )
                """
        
        with self.get_connection() as conn:
            conn.execute(sql)

    def insert(self, firstName, lastName, birthday, email, password):
        password = password.encode()
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password, salt)

        sql =   """
                INSERT INTO patientLog (firstName, lastName, birthday, email, password)
                VALUES (?, ?, ?, ?, ?)
                """
        
        params = (firstName, lastName, birthday, email, hashed_password)

        with self.get_connection() as conn:
            conn.execute(sql, params)

    def fetchall(self, sql):
        sql = "SELECT * FROM patientLog"

        with self.get_connection() as conn:
            return conn.execute(sql).fetchall()
    
    def getID(self, email):
        return self.fetchone("email", (email,))