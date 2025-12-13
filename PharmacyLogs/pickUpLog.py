from logSet import Log

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

    def markIsPickedUp(self, prescriptionID):
        sql =   """
                UPDATE pickUpLog
                SET isPickedUp = true
                WHERE prescriptionID = ?
                """

        params = (prescriptionID, )

        self.execute(sql, params)