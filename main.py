import warnings
warnings.filterwarnings("ignore")

from PyQt5 import QtWidgets, uic, QtGui, QtCore
import sys

from functions import *

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('design.ui', self)

        self.Browse_btn.clicked.connect(self.browse)

        self.Calculate_btn.clicked.connect(self.calculate)

        
        self.show()

    def browse(self):
        fm = QtWidgets.QFileDialog.getOpenFileName(None,'Browse File')
        filename = fm[0]
        if filename=='': return               
        self.Entry.setText(filename)
        #print('File Path:',filename)


    def calculate(self):
        filename=self.Entry.text()
        #print(filename)
        sim,rel,fe=solve(filename)
        S='Sim: '
        for i in range(len(sim)):
            S+=str(i+1)+'. '+str(round(sim[i],2))+'     '
        R='Rel: '
        for i in range(len(rel)):
            R+=str(i+1)+'. '+str(round(rel[i],2))+'     '
        F='Fea: '
        for i in range(len(fe)):
            F+=str(i+1)+'. '+str(round(fe[i],2))+'     '

        self.ans_1.setText(S)
        self.ans_2.setText(R)
        self.ans_3.setText(F)
        


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
