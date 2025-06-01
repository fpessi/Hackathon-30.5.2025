import sys

from GUI import StartWindow
from PyQt6.QtWidgets import QApplication


def main():
    """Starts the qt event loop
    """
    global app
    app = QApplication(sys.argv)
    start = StartWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
