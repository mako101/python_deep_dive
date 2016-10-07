from PyQt5.QtWidgets import QApplication
from MyDlg import MyDlg
import sys



def main():

    theApp = QApplication(sys.argv)
    dlg = MyDlg()
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