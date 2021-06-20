
from PySide2.QtCore import QCoreApplication, Qt
from PySide2.QtWidgets import QLineEdit, QPushButton, QVBoxLayout, QLabel, QWidget, QSpacerItem, QSizePolicy


class Form(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.line_edit = QLineEdit(
            placeholderText=self.tr("Email"))
        self.push_button = QPushButton(self)
        self.label = QLabel(
            text=self.tr("Отправить на почту"), alignment=Qt.AlignCenter
        )
        self.setup_ui()

    def setup_ui(self) -> None:
        """
        Инициализация ui.
        """

        self.label.setObjectName(u"label")
        self.line_edit.setObjectName(u"line_edit")
        self.push_button.setObjectName(u"push_button")
        self.push_button.setAutoFillBackground(True)
        self.setWindowTitle("Отправить по почте")
        self.push_button.setText(QCoreApplication.translate("Dialog", u"Отправить", None))
        vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        layout.addItem(vertical_spacer)
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.push_button)

        self.resize(320, 480)