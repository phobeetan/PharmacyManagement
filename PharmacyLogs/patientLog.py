import bcrypt
from PharmacyLogs import Log

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
                    password text,
                    email text UNIQUE,
                )
                """
        
        self.execute(sql)

    def insert(self, firstName, lastName, birthday, password, email):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        sql =   """
                INSERT INTO patientLog (firstName, lastName, birthday, password, email)
                VALUES (?, ?, ?, ?, ?)
                """
        
        params = (firstName, lastName, birthday, hashed_password, email)

        self.execute(sql, params)