import sys
from PySide6.QtWidgets import QApplication, QWidget
from gui.loginWindow import LoginWindow

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # login window
    window = LoginWindow()
    window.show()

    # starting the application
    sys.exit(app.exec())

if __name__ == "__main__":
    main()