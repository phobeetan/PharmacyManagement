import sqlite3
import bcrypt
from PharmacyLogs.logSet import Log

class Verify(Log):
    
    def __init__ (self, DB_PATH):
        super().__init__(DB_PATH)

    def validateEmail(self, email):
        return self.fetchone("email", (email,)) is None
    
    def validateName(self, name):
        invalids = "@0123456789~`!#$%^&*()_+=[]\\|{};':<>?,./\""
        for x in name:
            if x in invalids:
                return False
        return True #returns true if name is valid
    
    def getUserID(self, email):
        row = self.fetchone("email", (email,))
        return row[0] if row else None
    
    def getUserPassword(self, email):
        row = self.fetchone("email", (email,))
        return row[5] if row else None

    def verifyLogin(self, email, password):
        
        user_id = self.getUserID(email)

        if user_id is None:
            return False

        stored_hash = self.getUserPassword(user_id)

        if stored_hash is None:
            return False
        
        if isinstance(stored_hash, str):
            stored_hash = stored_hash.encode()
        
        return bcrypt.checkpw(password.encode(), stored_hash)
