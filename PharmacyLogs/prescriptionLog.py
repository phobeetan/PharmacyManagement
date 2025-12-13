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
                    needsRefill integer default 0,
                    endDate text default NULL
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

    def getPastMedications(self, patientID):
        sql =   """
                SELECT *
                WHERE patientID = ?, endDate
                FROM prescriptionLog
                """

        params = (patientID, )

        with self.get_connection() as conn:
            cursor = conn.cursor()
            return cursor.execute(sql, params).fetchall()