from pathlib import Path

from PySide2.QtCore import Qt, Signal
from PySide2.QtWidgets import QLineEdit, QPushButton, QVBoxLayout, QLabel, QWidget, QSpacerItem, QSizePolicy, \
    QPlainTextEdit, QHBoxLayout, QFileDialog, QGridLayout, QCheckBox


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
            placeholderText=self.tr("Email кому отправить: shiaz@yandex.ru"))
        self.text_lineedit = QPlainTextEdit(
            placeholderText=self.tr("Введите сообщение"))

        self.push_button = QPushButton(self.tr("Отправить"))
        self.label = QLabel(
            text=self.tr("Отправить на почту"), alignment=Qt.AlignCenter
        )
        self.image_path_widget = PathEdit()
        self.img_menu = ImgReaderMenu()
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
        layout.addWidget(self.image_path_widget)
        layout.addItem(vertical_spacer)
        layout.addWidget(self.label)
        layout.addWidget(self.addr_from_lineedit)
        layout.addWidget(self.password_lineedit)
        layout.addWidget(self.addr_to_lineedit)
        layout.addWidget(self.text_lineedit)
        layout.addWidget(self.push_button)

        # self.addr_from_lineedit.setEnabled(False)
        # self.password_lineedit.setEnabled(False)
        self.resize(320, 480)


class PathEdit(QWidget):
    path_changed = Signal(str)
    path = ""

    def __init__(self) -> None:
        QWidget.__init__(self)

        self.button = QPushButton("Выбрать файл")
        self.edit = QLineEdit(self.path)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.edit)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.openbox)

    def openbox(self) -> None:
        """
        Открытие окна выбора файла.
        """
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        filename, _ = dialog.getOpenFileName(self, "Open File",
                                             "",
                                             "Images (*.png *.xpm *.jpg)")

        self.path = Path(filename)
        self.edit.setText(self.path.name)
        self.path_changed.emit(str(self.path))

    def clear(self):
        self.edit.clear()


class ImgReaderMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QGridLayout()
        self.lable = QLabel("Меню ")
        self.read_img_button = QPushButton(self.tr("Прочесть"))
        self.check_box_processing = QCheckBox('Преобразовать', self)

        layout.addWidget(self.lable, 0, 0)
        layout.addWidget(self.read_img_button, 0, 1)
        layout.addWidget(self.check_box_processing, 1, 0)



