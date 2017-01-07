import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit)

class New_Player_Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('New Game')

        new_char_lbl = QLabel('Characer Name:', self)
        new_char_lbl.move(25,10)
        name_input = QLineEdit(self)
        name_input.move(50, 40)
        name_input

        self.show()



app = QApplication(sys.argv)

window = New_Player_Window()
sys.exit(app.exec_())