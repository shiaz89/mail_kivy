import sys

from PySide2.QtWidgets import QApplication

from presenter_mail import MailSender


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MailSender(app)
