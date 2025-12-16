from PyQt6.QtWidgets import QMainWindow, QMessageBox
from gui.ui_pharmacistView import Ui_MainWindow as PharmacistView
from gui.ui_pharmacistRegister import Ui_MainWindow as PharmacistRegister

from PharmacyLogs.pharmacistLog import pharmacistLog
from Users.pharmacist import Pharmacist

class PharmacistWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = PharmacistView()
        self.ui.setupUi(self)
        self.setWindowTitle("Pharmacist Dashboard")
        self.pharmacist = Pharmacist

        self.ui.inventorySubmit.clicked.connect(self.addMedicineToInventory)
        self.ui.assignSubmit.clicked.connect(self.assignPrescription)
        self.ui.updateSubmit.clicked.connect(self.updatePickUpStatus)

    def addMedicineToInventory(self):
        medicalName = self.ui.medicalNameEdit.text().strip()
        commonName = self.ui.commonNameEdit.text().strip()
        doseAmount = self.ui.doseAmountEdit.text().strip()
        bottleAmount = self.ui.bottleAmountEdit.text().strip()
        daysUse = self.ui.dayUseEdit.text().strip()
        doseUnits = self.ui.doseUnitEdit.text().strip()
        instructions = self.ui.instructionsEdit.text().strip()
        expiryDate = self.ui.expirationDateEdit.text().strip()

        if not (medicalName and commonName and doseAmount and bottleAmount and daysUse and doseUnits and instructions and expiryDate):
            QMessageBox.warning(self, "Error", "All fields are required.")
            return

        try:
            self.pharmacist.addInventory(medicalName, commonName, doseAmount, bottleAmount, daysUse, doseUnits, instructions, expirationDate)
            QMessageBox.information(self, "Success", "Medicine registered successfully!")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not register: {str(e)}")

    def assignPrescription(self):
        bottleID = self.ui.medicalNameEdit.text().strip()
        patientID = self.ui.commonNameEdit.text().strip()
        needsRefill = self.ui.doseAmountEdit.text().strip()

        if not (bottleID and patientID and needsRefill):
            QMessageBox.warning(self, "Error", "All fields are required.")
            return

        try:
            self.pharmacist.assignPrescription(bottleID, patientID, needsRefill)
            QMessageBox.information(self, "Success", "Medicine prescribed successfully!")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not register: {str(e)}")

    def updatePickUp(self, prescriptionID, pickUpDate):
        prescriptionID = self.ui.patientIDEdit.text().strip()
        pickUpDate = self.ui.pickUpDateEdit.text().strip()

        if not (prescriptionID and pickUpDate):
            QMessageBox.warning(self, "Error", "All fields are required.")
            return

        try:
            self.pharmacist.assignPrescription(prescriptionID, pickUpDate)
            QMessageBox.information(self, "Success", "PickUp logged successfully!")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not register: {str(e)}")


class PharmacistRegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = PharmacistRegister()
        self.ui.setupUi(self)
        self.setWindowTitle("Pharmacist Register")

        self.log = pharmacistLog()
        self.log.create_table()

        self.ui.pharmacisRegistertSubmit.clicked.connect(self.registerPharmacist)

    def registerPharmacist(self):
        firstName = self.ui.firstNameEdit.text().strip()
        lastName = self.ui.lastNameEdit.text().strip()
        email = self.ui.emailEdit.text().strip()
        password = self.ui.passwordEdit.text().strip()

        if not (firstName and lastName and email and password):
            QMessageBox.warning(self, "Error", "All fields are required.")
            return

        try:
            self.log.insert(None, firstName, lastName, email, password)
            QMessageBox.information(self, "Success", "Pharmacist registered successfully!")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not register: {str(e)}")