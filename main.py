import warnings
warnings.filterwarnings("ignore")

from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import sys

from functions import *

class Table(QWidget):
    def __init__(self,data):
        super().__init__()
        self.title = 'Table Data'
        self.left = 0
        self.top = 0
        self.width = 400
        self.height = 420
   
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.data=data
        
        self.createTable()
   
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
   
        self.center()
        
        self.show()
   
    #Create table
    def createTable(self):
        self.tableWidget = QTableWidget()
  
        #print(self.data[0])
        n=len((self.data)[0])
        
        
        self.tableWidget.setRowCount(n) 
  
        #print(self.data)
        self.tableWidget.setColumnCount(4)  
  
        self.tableWidget.setItem(0,0, QTableWidgetItem("Feature"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Sim"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Rel"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("Fe"))

        
        for i in range(1,n+1):
            self.tableWidget.setItem(i,0, QTableWidgetItem(str(self.data[3][i-1])))
            self.tableWidget.setItem(i,1, QTableWidgetItem(str(round(self.data[0][i-1],4))))
            self.tableWidget.setItem(i,2, QTableWidgetItem(str(round(self.data[1][i-1],4))))
            self.tableWidget.setItem(i,3, QTableWidgetItem(str(round(self.data[2][i-1],4))))
       
        #Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

        
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('design.ui', self)
        
        self.Browse_btn.clicked.connect(self.browse)

        self.Calculate_btn.clicked.connect(self.calculate)

        self.secondary_window=None
        
        self.show()

    def browse(self):
        fm = QtWidgets.QFileDialog.getOpenFileName(None,'Browse File')
        filename = fm[0]
        if filename=='': return               
        self.Entry.setText(filename)
        #print('File Path:',filename)


    def calculate(self):
        
        filename=self.Entry.text()
        feature_no=self.Feature_no.text()

        if feature_no=='':
            feature_no='1'
        feature_no=int(feature_no)
            
        #print(filename)
        #print(feature_no)
        
        sim,rel,fe,cols=solve(filename)
        data=[sim,rel,fe,cols]
        
        #print(data)
        Ans1=model_custom(feature_no,filename,fe,GaussianNB())
        Ans2=model_custom(feature_no,filename,fe,SVC())
        Ans3=model_custom(feature_no,filename,fe,tree.DecisionTreeClassifier())
        Ans4=model_custom(feature_no,filename,fe,RandomForestClassifier())

        #print(Ans1,Ans2,Ans3,Ans4)
        
        self.ans_1.setText('GaussianNB\t:\t'+str(Ans1))
        self.ans_2.setText('SVM\t\t:\t'+str(Ans1))
        self.ans_3.setText('Decision Tree\t:\t'+str(Ans1))
        self.ans_4.setText('Random Forest\t:\t'+str(Ans1))

        self.secondary_window=Table(data)
        self.secondary_window.show()
        
        


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
