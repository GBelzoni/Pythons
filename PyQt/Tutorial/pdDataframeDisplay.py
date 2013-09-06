'''
Created on Jan 10, 2013

@author: phcostello
'''


#Created by Patrick Costello 9 Jan 2013
#Boiler Plate

import math
import numpy as np
import scipy as sp
import pandas as pd
reload(pd)
import matplotlib.pyplot as plt

print pd.version.version

# <codecell>

#read data
path = '/home/phcostello/Dropbox/iHub/Umati/'
data = pd.read_csv(path + 'Decdata.csv')

import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

w = QtGui.QWidget()

df = data 

datatable = QtGui.QTableWidget(parent=w)
datatable.setColumnCount(len(df.columns))

datatable.setColumnCount(len(df.columns))
datatable.setRowCount(len(df.index))
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        datatable.setItem(i,j,QtGui.QTableWidgetItem(str(df.iget_value(i, j))))


datatable.resize(250, 150)
datatable.move(300, 300)
datatable.setWindowTitle('Simple')

datatable.show()
sys.exit(app.exec_())
datatable?

#self.datatable = QtGui.QTableWidget(parent=self)
#self.datatable.setColumnCount(len(df.columns))
#self.datatable.setRowCount(len(df.index))
#for i in range(len(df.index)):
 #   for j in range(len(df.columns)):
  #      self.datatable.setItem(i,j,QtGui.QTableWidgetItem(str(df.iget_value(i, j))))