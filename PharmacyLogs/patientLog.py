import sqlite3
import bcrypt
from logSet import Log

class patientLog(Log):

    #LOG MANAGEMENT
    def __init__(self):
        super().__init__("PharmacyLogs/patientLog.db")

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
        
        self.execute(sql)

    def insert(self, firstName, lastName, birthday, email, password):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        sql =   """
                INSERT INTO patientLog (firstName, lastName, birthday, email, password)
                VALUES (?, ?, ?, ?, ?)
                """
        
        params = (firstName, lastName, birthday, email, hashed_password)

        self.execute(sql, params)
    
    def getID(self, email):
        row = self.fetchone("email", (email,))
        return row[0] if row else None