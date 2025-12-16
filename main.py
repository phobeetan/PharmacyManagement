import sys
from PyQt6.QtWidgets import QApplication
from gui.loginWindow import PharmacistLoginWindow

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # login window
    window = PharmacistLoginWindow()
    window.show()

    # starting the application
    sys.exit(app.exec())

if __name__ == "__main__":
    main()