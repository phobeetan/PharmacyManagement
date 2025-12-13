import bcrypt
from logSet import Log

class pharmacistLog(Log):

    #LOG MANAGEMENT
    def __init__(self):
        super().__init__("PharmacyLogs/pharmacistLog.db")

    def create_table(self):
        sql =   """
                CREATE TABLE IF NOT EXISTS pharmacistLog (
                    patientID integer primary key,
                    firstName text,
                    lastName text,
                    email text UNIQUE,
                    password text
                )
                """

        self.execute(sql)

    def insert(self, firstName, lastName, email, password):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        sql =   """
                INSERT INTO pharmacistLog (firstName, lastName, email, password)
                VALUES (?, ?, ?, ?)
                """

        params = (firstName, lastName, email, hashed_password)

        self.execute(sql, params)