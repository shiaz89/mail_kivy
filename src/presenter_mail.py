import sys

from PySide2.QtWidgets import QApplication

from src.constants import TESSERACT_DIR
from src.img_to_str import ImgReader
from src.model import send_mail
from src.view import Form


class MailSender:
    def __init__(self, app: QApplication) -> None:
        self.form = Form()
        self.form.show()
        self.connect_signals()
        self.reader = ImgReader(TESSERACT_DIR)
        sys.exit(app.exec_())

    def connect_signals(self) -> None:
        self.form.push_button.clicked.connect(self.click_send_mail)
        self.form.image_path_widget.path_changed.connect(self.change_img_path)

    def click_send_mail(self) -> None:
        addr_from = self.form.addr_from_lineedit.text() if self.form.addr_from_lineedit.text() else "shiaz@yandex.ru"
        password = self.form.password_lineedit.text() if self.form.password_lineedit.text() else "siz035036503530"

        addr_to = self.form.addr_to_lineedit.text() if self.form.addr_to_lineedit.text() else "shiaz@yandex.ru"

        text = self.form.text_lineedit.toPlainText()
        text = text if text else "Ничего не ввел"
        send_mail(addr_from=addr_from, addr_to=addr_to, password=password, text_msg=text)
        self.form.text_lineedit.clear()
        self.form.image_path_widget.cleer()


    def change_img_path(self, img_path: str) -> None:
        """
        Если изменился путь к картинке, то идет запись в поле пути до картинки
        и разбор изображения на слова. При перезагрузке сообщение обнавляется.

        :param img_path: Путь до изображения.
        """
        img_str = self.reader.read_img(img_path, "rus")
        self.form.text_lineedit.setPlainText(f"Текст с картинки:")
        self.form.text_lineedit.appendPlainText(img_str)
