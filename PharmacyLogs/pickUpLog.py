from logSet import Log
from datetime import datetime, timedelta

class pickUpLog(Log):

    #LOG MANAGEMENT
    def __init__(self):
        super().__init__("PharmacyLogs/pickUpLog.db")

    def create_table(self):
        sql =   """
                CREATE TABLE IF NOT EXISTS pickUpLog (
                    prescriptionID integer primary key,
                    pickUpDate text,
                    isPickedUp integer default 0,
                    endDate integer
                )
                """

        self.execute(sql)

    def insert(self, prescriptionID, pickUpDate, endDate):
        sql =   """
                INSERT INTO pickUpLog (prescriptionID, pickUpDate, endDate)
                VALUES (?, ?, ?)
                """

        params = (prescriptionID, pickUpDate, endDate)

        self.execute(sql, params)

    def markIsPickedUp(self, prescriptionID, pickUpDate):
        #get bottle id from prescriptoinlog, get daysUse from inventory, add to current date.
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

        sql =   """
                UPDATE pickUpLog
                SET isPickedUp = 1, pickUpDate = ?, endDate = ?
                WHERE prescriptionID = ?
                """

        params = (pickUpDate.isoformat(), endDate.isoformat(), prescriptionID)

        self.execute(sql, params)