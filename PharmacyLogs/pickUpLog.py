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
                    isPickedUp boolean,
                    endDate integer,
                )
                """

        self.execute(sql)

    def insert(self, prescriptionID, pickUpDate, isPickedUp, endDate):
        sql =   """
                INSERT INTO pickUpLog (prescriptionID, pickUpDate, isPickedUp, endDate)
                VALUES (?, ?, ?)
                """

        params = (prescriptionID, pickUpDate, isPickedUp, endDate)

        self.execute(sql, params)