'''
Created on Jan 10, 2013

@author: phcostello
'''
import sys
from PyQt4.QtGui import *

lista = ['aa', 'ab', 'ac']
listb = ['ba', 'bb', 'bc']
listc = ['ca', 'cb', 'cc']
mystruct = {'A':lista, 'B':listb, 'C':listc}


class MyTable(QTableWidget):
    def __init__(self, thestruct, *args):
        QTableWidget.__init__(self, *args)
        self.data = thestruct
    
    def setmydata(self):
        n = 0
        for key in self.data:
            m = 0
            for item in self.data[key]:
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
                m += 1
            n += 1
    
    def showTable(self,args):
        
        app = QApplication(args)
        self.setmydata()
        #self.show()
        app.exec_()
            
def main(args):
    app = QApplication(args)
    table = MyTable(mystruct, 5, 3)
    table.show()
    app.exec_()
    
def main2():
    
    table = MyTable(mystruct,5,3)
    table.showTable(sys.argv)
    
if __name__=="__main__":
    main(sys.argv)
#    main2()

