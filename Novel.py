import random

import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from untitled import Ui_Form
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, qApp, QStyleFactory
from Figure_Canvas import Figure_Canvas
from PCA import myPCA


class mywindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        qApp.setStyle(QStyleFactory.create('Fusion'))
        self.coef_varience = 0
        self.coef_mean = 1
        self.rand_target = None
        self.input_y = None
        self.ax = None
        self.graphicscene = None
        self.drOld = None
        self.input_x = None
        self.rand_data = None
        self.pca = myPCA()
        self.class_n = 3
        self.single_class_n = 50
        self.sample_feature_n = 4
        self.setupUi(self)
        self.showNoGraph()
        self.pushButton.clicked.connect(self.on_click)
        self.rand.clicked.connect(self.on_rand_click)
        self.setInputTableView()
        self.coefficient_of_mean_value.setValue(1)
        self.number_of_features.setValue(4)
        self.number_of_classes.setValue(3)
        self.number_of_each_class.setValue(50)
        self.progressBar.setValue(0)





    def setInputTableView(self):
        self.model = QStandardItemModel(self.class_n * self.single_class_n, self.sample_feature_n+1)
        headlist = list()
        for i in range(self.sample_feature_n):
            headlist.append('f'+str(i+1))
        headlist.append('y')
        self.model.setHorizontalHeaderLabels(headlist)
        for i in range(self.class_n * self.single_class_n):
            for j in range(self.sample_feature_n):
                self.model.setItem(i, j, QStandardItem(str(self.pca.x[i][j])))
        for i in range(self.class_n * self.single_class_n):
            self.model.setItem(i, self.sample_feature_n, QStandardItem(str(self.pca.y[i])))
        self.input_data.setModel(self.model)
        for i in range(self.class_n * self.single_class_n):
            self.input_data.setRowHeight(i, 1)
        for j in range(self.sample_feature_n+1):
            self.input_data.setColumnWidth(j, 35)

    def showNoGraph(self):
        self.drOld = Figure_Canvas()
        self.graphicscene = QtWidgets.QGraphicsScene()
        self.graphicscene.addWidget(self.drOld)
        self.graphicsView.setScene(self.graphicscene)
        self.graphicsView.show()

    @pyqtSlot()
    def on_click(self):
        self.refreshInput()
        self.PCA_normal_start()
        self.progressBar.setValue(10)
        self.PCA_graph_show()
        self.progressBar.setValue(50)
        self.setOuputTableView()
        self.progressBar.setValue(70)
        self.setOutPutText()
        self.progressBar.setValue(100)

    @pyqtSlot()
    def on_rand_click(self):
        self.pushButton.setEnabled(False)
        self.getChoice()
        self.number_of_classes.setReadOnly(True)
        self.randData()
        self.PCA_rand_start()
        self.setInputTableView()
        self.progressBar.setValue(10)
        self.PCA_graph_show()
        self.progressBar.setValue(50)
        self.setOuputTableView()
        self.progressBar.setValue(70)
        self.setOutPutText()
        self.progressBar.setValue(100)
        self.number_of_classes.setReadOnly(False)

    def PCA_normal_start(self):
        self.pca.refreshData(self.input_x, self.input_y)
        self.pca.doPCA()

    def PCA_rand_start(self):
        self.pca.refreshData(self.rand_data, self.rand_target)
        self.pca.doPCA()

    def PCA_graph_show(self):
        self.drOld = Figure_Canvas()
        self.graphicscene = QtWidgets.QGraphicsScene()
        self.graphicscene.addWidget(self.drOld)
        print(self.pca.class_dict_x[1])
        for i in self.pca.class_dict_x.keys():
            color ='#'+(str(hex(random.randint(0,256*256*256)).split('0x')[1])).rjust(6,'0')
            print(color)
            self.drOld.axes.scatter(self.pca.class_dict_x[i],self.pca.class_dict_y[i],c=color,marker='.')


        # self.drOld.axes.scatter(self.pca.red_x, self.pca.red_y, c='r', marker='.')
        # self.drOld.axes.scatter(self.pca.blue_x, self.pca.blue_y, c='b', marker='.')
        # self.drOld.axes.scatter(self.pca.green_x, self.pca.green_y, c='g', marker='.')
        self.graphicsView.setScene(self.graphicscene)
        self.graphicsView.show()

    def setOuputTableView(self):
        self.model_out = QStandardItemModel(150, 3)
        self.model_out.setHorizontalHeaderLabels(['r1', 'r2', 'y'])
        for i in range(150):
            for j in range(2):
                self.model_out.setItem(i, j, QStandardItem(str(self.pca.reduced_x[i][j])))
        for i in range(150):
            self.model_out.setItem(i, 2, QStandardItem(str(self.pca.y[i])))
        self.output_data.setModel(self.model_out)
        for i in range(150):
            self.output_data.setRowHeight(i, 1)
        for j in range(3):
            self.output_data.setColumnWidth(j, 55)

        print(eval(self.model_out.item(1, 1).text()))

    def setOutPutText(self):
        self.explained_varience_value.setText(str(self.pca.explained_variance))
        self.explained_varience_ratio_value.setText(str(self.pca.explained_variance_ratio))
        self.noise_variance_value.setText(str(self.pca.noise_variance))
        self.n_components_value.setText(str(self.pca.n_components))

    def refreshInput(self):
        in_xlist = []
        in_ylsit = []
        for i in range(150):
            temp = []
            for j in range(4):
                temp.append(eval(self.model.item(i, j).text()))
            in_xlist.append(temp)
        for i in range(150):
            in_ylsit.append(eval(self.model.item(i, 4).text()))
        self.input_x = np.array(in_xlist)
        self.input_y = np.array(in_ylsit)

    def randData(self):
        self.rand_data = np.zeros((self.class_n * self.single_class_n, self.sample_feature_n))
        for i in range(self.class_n):
            for j in range(self.sample_feature_n):
                self.rand_data[i*self.single_class_n:(i + 1) * self.single_class_n, j] = np.random.normal(i*self.coef_mean, random.random()*(1+self.coef_varience), self.single_class_n).T
        self.rand_target = np.zeros(self.class_n * self.single_class_n)
        for i in range(self.class_n):
            self.rand_target[i*self.single_class_n:(i + 1) * self.single_class_n] = i
        print(np.shape(self.rand_data))
        print(np.shape(self.rand_target))

    def getChoice(self):
        self.class_n = eval(self.number_of_classes.text())
        self.sample_feature_n =eval(self.number_of_features.text())
        self.single_class_n = eval(self.number_of_each_class.text())
        self.coef_mean = eval(self.coefficient_of_mean_value.text())
        self.coef_varience = eval(self.coefficient_of_varience.text())

        # self.sample_feature_n = 7



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())
