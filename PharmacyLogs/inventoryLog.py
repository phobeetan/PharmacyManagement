from PharmacyLogs import Log

class inventoryLog(Log):

    #LOG MANAGEMENT
    def __init__(self):
        super().__init__("PharmacyLogs/inventoryLog.db")

    def create_table(self):
        sql =   """
                CREATE TABLE IF NOT EXISTS inventoryLog (
                    bottleID integer primary key,
                    medicalName text,
                    commonName text,
                    doseAmount integer,
                    bottleAmount integer,
                    daysUse integer,
                    doseUnits text,
                    instructions text,
                    expirationDate text
                )
                """

        self.execute(sql)

    def insert(self, medicalName, commonName, doseAmount, bottleAmount, daysUse, doseUnits, instructions, expirationDate):
        sql =   """
                INSERT INTO inventoryLog (medicalName, commonName, doseAmount, bottleAmount, daysUse, doseUnits, instructions, expirationDate)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """

        params = (medicalName, commonName, doseAmount, bottleAmount, daysUse, doseUnits, instructions, expirationDate)

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            return cursor.lastrowid