from verify import Verify
from datetime import datetime, timedelta
from PharmacyLogs.pharmacistLog import pharmacistLog
from PharmacyLogs.inventoryLog import inventoryLog
from PharmacyLogs.prescriptionLog import prescriptionLog
from PharmacyLogs.pickUpLog import pickUpLog

global_pharmacist = pharmacistLog()
global_inventory = inventoryLog()
global_prescription = prescriptionLog()
global_pickUp = pickUpLog()

class Pharmacist(Verify):
    pharmacist = global_pharmacist
    inventory = global_inventory
    prescription = global_prescription
    pickUp = global_pickUp

    def __init__(self, pharmacistID, email, firstName, lastName, password):
        self.verify = Verify(pharmacist.DB_PATH)
        self.email = email

        # Validate
        if not self.verify.validateEmail(email):
            raise ValueError("Email Already Exists")
        if not self.verify.validateName(firstName) or not self.verify.validateName(lastName):
            raise ValueError("Invalid Characters in Name")

        # Register
        self.pharmacist.insert(pharmacistID, email, firstName, lastName, password)

    def addInventory(self, medicalName, commonName, doseAmount, bottleAmount, daysUse, doseUnits, instructions, expirationDate):
        bottleID = self.inventory.insert(medicalName, commonName, doseAmount, bottleAmount, daysUse, doseUnits, instructions, expirationDate)
        print(bottleID)

    def assignPrescription(self, bottleID, patientID, needsRefill=0):
        prescriptionID = self.prescription.insert(bottleID, patientID, needsRefill)
        print(prescriptionID)

    def updatePickUp(self, prescriptionID, pickUpDate):
        pickUpDate = datetime.fromisoformat(pickUpDate)
        self.pickUp.markPickedUp(prescriptionID, pickUpDate)