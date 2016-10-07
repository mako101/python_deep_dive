from PyQt5.QtWidgets import QDialog, QPushButton
from PyQt5.QtWidgets import QHBoxLayout

class MyDlg(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        bttn1 = QPushButton('Button 1')
        bttn2 = QPushButton('Button 2')
        bttn3 = QPushButton('Button 3')

        layout = QHBoxLayout()

        layout.addWidget(bttn1)
        layout.addWidget(bttn2)
        layout.addWidget(bttn3)

        self.setLayout(layout)
