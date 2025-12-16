from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui_loginWindow import Ui_MainWindow
from Users.verify import Verify

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Login")
        self.ui.loginButton.clicked.connect(self.login)