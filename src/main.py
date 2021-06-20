import sys

from PySide2.QtWidgets import QApplication, QDialog

from src.view import Form

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
