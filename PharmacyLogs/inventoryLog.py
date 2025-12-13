import bcrypt
from logSet import Log


class inventoryLog(Log):

    # LOG MANAGEMENT
    def __init__(self):
        super().__init__("PharmacyLogs/inventoryLog.db")

    def create_table(self):
        sql = """ \
              CREATE TABLE IF NOT EXISTS inventoryLog \
              ( \
                  patientID \
                  integer \
                  primary \
                  key, \
                  firstName \
                  text, \
                  lastName \
                  text, \
                  birthday \
                  text, \
                  email \
                  text \
                  UNIQUE, \
                  password \
                  text \
              )
                """

        self.execute(sql)

    def insert(self, firstName, lastName, birthday, email, password):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        sql = """ \
              INSERT INTO inventoryLog (firstName, lastName, birthday, email, password) \
              VALUES (?, ?, ?, ?, ?)
                """

        params = (firstName, lastName, birthday, email, hashed_password)

        self.execute(sql, params)