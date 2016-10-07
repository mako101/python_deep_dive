from PyQt5.QtWidgets import (
    QDialog, QPushButton, QGridLayout,
    QToolTip)
from PyQt5.QtGui import QIcon, QFont


class MyGrid(QDialog):

    def __init__(self):
        QDialog.__init__(self)

        self.setWindowTitle('My Grid App')
        self.setWindowIcon(QIcon('icon.png'))

        layout = QGridLayout()
        layout.setSpacing(10)
        self.setLayout(layout)

        # Tooltip for the main app window
        QToolTip.setFont(QFont('Times New Roman', 12))
        self.setToolTip('<b>Hi!</b>')

        # Button 1 -> Button 10
        button_names = ['Button {}'.format(i) for i in range(1, 11)]

        # 2 rows and 5 columns
        positions = [(row, column) for row in range(2) for column in range(5)]

        # Construct a grid
        for button_name, position in zip(button_names, positions):
            button = QPushButton(button_name)
            # Change the font of all buttons
            button.setFont(QFont('ComicSans', 18))
            # Set custom tooltip for each button
            button.setToolTip('<i>{}</i>'.format(button_name))
            layout.addWidget(button, *position)
