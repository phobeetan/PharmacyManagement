from verify import Verify
from PharmacyLogs.pharmacistLog import pharmacistLog
from PharmacyLogs.inventoryLog import inventoryLog
from PharmacyLogs.prescriptionLog import prescriptionLog

global_pharmacist = pharmacistLog()
global_inventory = inventoryLog()
global_prescription = prescriptionLog()


class Pharmacist(Verify):
    inventory = global_inventory
    prescription = global_prescription

    def __init__(self, pharmacistID, email, firstName, lastName, password):
        self.verify = Verify(global_pharmacist.DB_PATH)
        self.email = email

        # Validate
        if not self.verify.validateEmail(email):
            raise ValueError("Email Already Exists")
        if not self.verify.validateName(firstName) or not self.verify.validateName(lastName):
            raise ValueError("Invalid Characters in Name")

        # Register
        self.global_pharmacist.insert(pharmacistID, email, firstName, lastName, password)

    def addInventory(self, medicalName, commonName, doseAmount, bottleAmount, daysUse, doseUnits, instructions, expirationDate):
        self.inventory.insert(medicalName, commonName, doseAmount, bottleAmount, daysUse, doseUnits, instructions, expirationDate)

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            return cursor.lastrowid

    def fetchone(self, column, param=()):
        sql = "SELECT * FROM Log WHERE " + column + " = ?"

        with self.get_connection() as conn:
            cursor = conn.cursor()
            return cursor.execute(sql, param).fetchone()

    def assignMedicine(self, bottleID, patientID, needsRefill=0):
        self.prescription.insert(bottleID, patientID, needsRefill)

