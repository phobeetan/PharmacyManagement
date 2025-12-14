# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from login_window import LoginWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_pharmdatabase

class pharmdatabase(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_pharmdatabase()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = pharmdatabase()
    widget.show()
    sys.exit(app.exec())

def main():
    """Zamaibe Pharmacy Application"""
    app = QApplication(sys.argv)

    # setting application style
    app.setStyle("Fusion")
    # login window
    window = LoginWindow()
    window.show()
    # starting the application
    sys.exit(app.exec())

    if __name__ == "__main__":
        main()
