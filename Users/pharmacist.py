from verify import Verify
from datetime import datetime
from PharmacyLogs import pharmacistLog, inventoryLog, prescriptionLog, pickUpLog

global_pharmacist = pharmacistLog.pharmacistLog()
global_inventory = inventoryLog.inventoryLog()
global_prescription = prescriptionLog.prescriptionLog()
global_pickUp = pickUpLog.pickUpLog()

class Pharmacist(Verify):
    pharmacist = global_pharmacist
    inventory = global_inventory
    prescription = global_prescription
    pickUp = global_pickUp

    def __init__(self, pharmacistID, email, firstName, lastName, password):
        self.verify = Verify(self.pharmacist.DB_PATH)
        self.email = email

        # Validate
