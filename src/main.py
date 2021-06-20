import sys

from PySide2.QtWidgets import QApplication, QDialog

from src.presenter_mail import MailSender
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MailSender(app)
