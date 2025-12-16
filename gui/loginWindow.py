from PyQt6.QtWidgets import QMainWindow, QLineEdit, QMessageBox
from gui.ui_loginWindow import Ui_MainWindow
from gui.pharmacistWindow import PharmacistWindow, PharmacistRegisterWindow

from Users.verify import Verify
from PharmacyLogs.pharmacistLog import pharmacistLog
from PharmacyLogs.patientLog import patientLog

class BaseLoginWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(title)

        self.ui.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.registerButton.clicked.connect(self.register)

    def login(self):
        QMessageBox.information(self, "Login", "Login handled elsewhere.")

    def register(self):
        QMessageBox.information(self, "Register", "Registration handled elsewhere.")

    def error(self, message):
        QMessageBox.critical(self, "Login Failed", message)

class PharmacistLoginWindow(BaseLoginWindow):
    def __init__(self):
        super().__init__("Pharmacist Login")

        self.pharmacist = pharmacistLog()
        self.pharmacist.create_table()
        self.verifier = Verify(self.pharmacist, "pharmacistLog")

    def login(self):
        identifier = self.ui.username.text().strip()
        password = self.ui.password.text()

        if not identifier or not password:
            self.error("Both fields are required.")
            return

        if self.verifier.verifyLogin(identifier, password):
            self.dashboard = PharmacistWindow()
            self.dashboard.show()
            self.close()
        else:
            self.error("Incorrect credentials.")

    def register(self):
        self.dashboard = PharmacistRegisterWindow()
        self.dashboard.show()
        self.close()

class PatientLoginWindow(BaseLoginWindow):
    def __init__(self):
        super().__init__("Patient Login")

        self.log = patientLog()
        self.verifier = Verify(self.log.DB_PATH)

    def login(self):
        identifier = self.ui.username.text().strip()
        password = self.ui.password.text()

        if not identifier or not password:
            self.error("Both fields are required.")
            return

        if self.verifier.verifyLogin(identifier, password):
            QMessageBox.information(self, "Success", "Patient login successful.")
            self.close()
        else:
            self.error("Incorrect email or password.")

    def register(self):
        QMessageBox.information(self, "Register", "Registration handled elsewhere.")