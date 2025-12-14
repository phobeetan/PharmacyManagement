from logSet import Log
from datetime import datetime

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

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            return cursor.lastrowid

    def getPastMedications(self, patientID):
        today = datetime.today().date().isoformat()

        sql =   """
                SELECT *
                FROM prescriptionLog
                WHERE patientI