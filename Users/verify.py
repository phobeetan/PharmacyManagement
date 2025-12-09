import sqlite3

class Verify:
    
    def __init__ (self, db_path, table_name, id_column)
        self.db_path = db_path
        self.table_name = table_name
        self.id_column = id_column
    
    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def validateEmail(self, email):
        #check if email availible
        connect = self.get_connection()
        cur = connect.cursor()
        cur.execute(
            f"SELECT 1 FROM {self.table_name} WHERE email = ?".
            (email,)
        )
        exists = cur.fetchone()
        connect.close()
        return not exists #returns true if email is availible
    
    def validateName(self, name):
        invalids = "@0123456789~`!#$%^&*()_+=[]\\|{};':<>?,./\""
        for x in name:
            if x in invalid_chars:
                return False
        return True #returns true if name is valid

    

