from PyQt5.QtWidgets import QApplication
from MyDlg import MyGrid
import sys



def main():

    theApp = QApplication(sys.argv)
    dlg = MyGrid()
    dlg.show()

    theApp.exec()



main()




# dlg.se
# theDlg.show()
#
# theApp.exec()



# app has:

#  event loop to listen to events
# event handlet to reposnd ot them