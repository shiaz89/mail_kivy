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
        addr_from = self.form.addr_from_lineedit.text() if self.form.addr_from_lineedit.text() else "shiaz@yandex.ru"
        password = self.form.password_lineedit.text() if self.form.password_lineedit.text() else "siz035036503530"

        addr_to = self.form.addr_to_lineedit.text() if self.form.addr_to_lineedit.text() else "shiaz@yandex.ru"

        text = self.form.text_lineedit.toPlainText()
        text = text if text else "Ничего не ввел"
        send_mail(addr_from=addr_from, addr_to=addr_to, password=password, text_msg=text)
