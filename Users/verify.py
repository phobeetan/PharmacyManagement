import sqlite3
import bcrypt
from PharmacyLogs.logSet import Log

class Verify(Log):
    def __init__(self, log, table_name):
        self.log = log
        self.table = table_name
        self.log.create_table()

    def validateEmail(self, email):
        return self.fetchone("email", (email,)) is None
    
    def validateName(self, name):
        invalids = "@0123456789~`!#$%^&*()_+=[]\\|{};':<>?,./\""
        for x in name:
            if x in invalids:
                return False
        return True #returns true if name is valid

    def getUserByEmail(self, email):
        sql = f"SELECT * FROM {self.table} WHERE email = ?"
        with self.log.get_connection() as conn:
            cursor = conn.cursor()
            return cursor.execute(sql, (email,)).fetchone()

    def getUserPassword(self, email):
        row = self.getUserByEmail(email)
        return row[4] if row else None

    def verifyLogin(self, email, password):
        
        row = self.getUserByEmail(email)

        if not row:
            return False

        stored_hash = self.getUserPassword(email)
        
        if isinstance(stored_hash, str):
            stored_hash = stored_hash.encode()
        
        return bcrypt.checkpw(password.encode(), stored_hash)
