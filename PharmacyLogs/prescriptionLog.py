from logSet import Log

class prescriptionLog(Log):

    #LOG MANAGEMENT
    def __init__(self):
        super().__init__("PharmacyLogs/prescriptionLog.db")

    def create_table(self):
        sql =   """
                CREATE TABLE IF NOT EXISTS prescriptionLog (
                    prescriptionID integer primary key,
                    bottleID text,
                    patientID text,
                    needsRefill boolean,
                )
                """

        self.execute(sql)

    def insert(self, bottleID, patientID, needsRefill):
        sql =   """
                INSERT INTO prescriptionLog (bottleID, patientID, needsRefill)
                VALUES (?, ?, ?)
                """

        params = (bottleID, patientID, needsRefill)

        self.execute(sql, params)