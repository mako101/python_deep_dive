from PyQt5.QtWidgets import QDialog, QPushButton, QSizePolicy
from PyQt5.QtWidgets import QVBoxLayout

class MyDlg(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        bttn1 = QPushButton('Button 1')
        bttn2 = QPushButton('Button 2')
        bttn3 = QPushButton('Button 3')
        bttn4 = QPushButton('Button 4')
        bttn5 = QPushButton('Button 5')

        bttn1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bttn5.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout = QVBoxLayout()

        layout.addWidget(bttn1)
        layout.addWidget(bttn2)
        layout.addWidget(bttn3)
        layout.addWidget(bttn4)
        layout.addWidget(bttn5)

        self.setWindowTitle('Vertical Box Layout')

        self.setLayout(layout)