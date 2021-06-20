
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QLineEdit, QPushButton, QVBoxLayout, QLabel, QWidget, QSpacerItem, QSizePolicy, \
    QPlainTextEdit


class Form(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.addr_from_lineedit = QLineEdit(
            placeholderText=self.tr("Email пользователя: shiaz@yandex.ru")
        )
        self.password_lineedit = QLineEdit(
            placeholderText=self.tr("Password"), echoMode=QLineEdit.Password
        )
        self.addr_to_lineedit = QLineEdit(
            placeholderText=self.tr("Email: shiaz@yandex.ru"))
        self.text_lineedit = QPlainTextEdit(
            placeholderText=self.tr("Введите сообщение"))

        self.push_button = QPushButton(self.tr("Отправить"))
        self.label = QLabel(
            text=self.tr("Отправить на почту"), alignment=Qt.AlignCenter
        )
        self.setup_ui()

    def setup_ui(self) -> None:
        """
        Инициализация ui.
        """

        self.label.setObjectName(u"label")
        self.addr_to_lineedit.setObjectName(u"addr_to_lineedit")
        self.push_button.setObjectName(u"push_button")
        self.push_button.setAutoFillBackground(True)
        self.setWindowTitle("Отправить по почте")
        vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        layout.addItem(vertical_spacer)
        layout.addWidget(self.label)
        layout.addWidget(self.addr_from_lineedit)
        layout.addWidget(self.password_lineedit)
        layout.addWidget(self.addr_to_lineedit)
        layout.addWidget(self.text_lineedit)
        layout.addWidget(self.push_button)

        self.resize(320, 480)