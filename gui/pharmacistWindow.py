from PyQt6.QtWidgets import QMainWindow, QMessageBox
from gui.ui_pharmacistView import Ui_MainWindow as PharmacistView
from gui.ui_pharmacistRegister import Ui_MainWindow as PharmacistRegister

from PharmacyLogs.pharmacistLog import pharmacistLog

class PharmacistWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = PharmacistView()
        self.ui.setupUi(self)
        self.setWindowTitle("Pharmacist Dashboard")

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