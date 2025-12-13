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

        self.execute(sql, params)

    def getPastMedications(self, patientID):
        today = datetime.today().date().isoformat()

        sql =   """
                SELECT *
                FROM prescriptionLog
                WHERE patientID = ?, endDate <= ?
                """

        params = (patientID, today)

        with self.get_connection() as conn:
            cursor = conn.cursor()
            return cursor.execute(sql, params).fetchall()