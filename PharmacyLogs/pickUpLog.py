from PharmacyLogs import Log
from datetime import datetime, timedelta

class pickUpLog(Log):

    #LOG MANAGEMENT
    def __init__(self):
        super().__init__("PharmacyLogs/pickUpLog.db")

    def create_table(self):
        sql =   """
                CREATE TABLE IF NOT EXISTS pickUpLog (
                    prescriptionID integer primary key,
                    pickUpDate text default NULL
                )
                """

        self.execute(sql)

    def insert(self, prescriptionID):
        sql =   """
                INSERT INTO pickUpLog (prescriptionID)
                VALUES (?)
                """

        params = (prescriptionID, )

        self.execute(sql, params)

    def markPickedUp(self, prescriptionID, pickUpDate):
        sql = "SELECT bottleID FROM prescriptionLog WHERE prescriptionID = ?"
        with self.get_connection() as conn:
            cursor = conn.cursor()
            bottleID = cursor.execute(sql, (prescriptionID, )).fetchone()[0]

        sql = "SELECT daysUse FROM inventoryLog WHERE bottleID = ?"
        with self.get_connection() as conn:
            cursor = conn.cursor()
            daysUse = cursor.execute(sql, (bottleID, )).fetchone()[0]

        pickUpDate = datetime.fromisoformat(pickUpDate)
        endDate = pickUpDate + timedelta(days=daysUse)

        sql =   "UPDATE prescriptionLog SET endDate = ? WHERE prescriptionID = ?"
        self.execute(sql, (endDate.isoformat(), prescriptionID))

        sql = "UPDATE pickUpLog SET pickUpDate = ? WHERE prescriptionID = ?"
        self.execute(sql, (pickUpDate.isoformat(), prescriptionID))