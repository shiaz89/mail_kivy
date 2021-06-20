import sys

from PySide2.QtWidgets import QApplication

from src.model import send_mail
from src.view import Form


class MailSender():
    def __init__(self, app: QApplication):
        self.form = Form()
        self.form.show()
        self.connect_signals()
        sys.exit(app.exec_())

    def connect_signals(self):
        self.form.push_button.clicked.connect(self.click_send_mail)

    def click_send_mail(self):
        addr_to = self.form.line_edit.text() if self.form.line_edit.text() else "shiaz@yandex.ru"
        send_mail(addr_to=addr_to)