import bcrypt
from PharmacyLogs import Log

class pharmacistLog(Log):

    #LOG MANAGEMENT
    def __init__(self):
        self.DB_PATH = "PharmacyLogs/pharmacistLog.db"
        super().__init__(self.DB_PATH)

    def create_table(self):
        sql =   """
                CREATE TABLE IF NOT EXISTS pharmacistLog (
                    pharmacistID integer primary key,
                    firstName text,
                    lastName text,
                    email text UNIQUE,
                    password text
                )
                """

        self.execute(sql)

    def insert(self, pharmacistID, firstName, lastName, email, password):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        sql =   """
                INSERT INTO pharmacistLog (pharmacistID, firstName, lastName, email, password)
                VALUES (?, ?, ?, ?, ?)
                """

        params = (pharmacistID, firstName, lastName, email, hashed_password)

        self.execute(sql, params)