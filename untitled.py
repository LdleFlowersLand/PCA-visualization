# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(929, 686)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 931, 691))
        self.tabWidget.setStyleSheet("baclground-color:rgb(255, 255, 255)")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(330, 10, 531, 271))
        self.graphicsView.setStyleSheet("background-color:rgb(255, 255, 255,0)")
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphicsView.setLineWidth(0)
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 231, 31))
        self.pushButton.setObjectName("pushButton")
        self.explained_varience = QtWidgets.QLabel(self.tab)
        self.explained_varience.setGeometry(QtCore.QRect(30, 400, 121, 31))
        self.explained_varience.setObjectName("explained_varience")
        self.explained_varience_value = QtWidgets.QLabel(self.tab)
        self.explained_varience_value.setGeometry(QtCore.QRect(30, 430, 231, 21))
        self.explained_varience_value.setText("")
        self.explained_varience_value.setObjectName("explained_varience_value")
        self.input_data = QtWidgets.QTableView(self.tab)
        self.input_data.setGeometry(QtCore.QRect(350, 300, 231, 321))
        self.input_data.setObjectName("input_data")
        self.output_data = QtWidgets.QTableView(self.tab)
        self.output_data.setGeometry(QtCore.QRect(610, 300, 231, 321))
        self.output_data.setObjectName("output_data")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(30, 590, 271, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.explained_varience_ratio = QtWidgets.QLabel(self.tab)
        self.explained_varience_ratio.setGeometry(QtCore.QRect(30, 440, 161, 31))
        self.explained_varience_ratio.setObjectName("explained_varience_ratio")
        self.explained_varience_ratio_value = QtWidgets.QLabel(self.tab)
        self.explained_varience_ratio_value.setGeometry(QtCore.QRect(30, 470, 231, 21))
        self.explained_varience_ratio_value.setText("")
        self.explained_varience_ratio_value.setObjectName("explained_varience_ratio_value")
        self.noise_variance = QtWidgets.QLabel(self.tab)
        self.noise_variance.setGeometry(QtCore.QRect(30, 480, 161, 31))
        self.noise_variance.setObjectName("noise_variance")
        self.noise_variance_value = QtWidgets.QLabel(self.tab)
        self.noise_variance_value.setGeometry(QtCore.QRect(30, 510, 231, 21))
        self.noise_variance_value.setText("")
        self.noise_variance_value.setObjectName("noise_variance_value")
        self.n_components = QtWidgets.QLabel(self.tab)
        self.n_components.setGeometry(QtCore.QRect(30, 520, 161, 31))
        self.n_components.setObjectName("n_components")
        self.n_components_value = QtWidgets.QLabel(self.tab)
        self.n_components_value.setGeometry(QtCore.QRect(30, 550, 231, 21))
        self.n_components_value.setText("")
        self.n_components_value.setObjectName("n_components_value")
        self.rand = QtWidgets.QPushButton(self.tab)
        self.rand.setGeometry(QtCore.QRect(30, 70, 231, 31))
        self.rand.setObjectName("rand")
        self.before_PCA = QtWidgets.QLabel(self.tab)
        self.before_PCA.setGeometry(QtCore.QRect(350, 280, 81, 16))
        self.before_PCA.setObjectName("before_PCA")
        self.after_PCA = QtWidgets.QLabel(self.tab)
        self.after_PCA.setGeometry(QtCore.QRect(610, 280, 81, 16))
        self.after_PCA.setObjectName("after_PCA")
        self.number_of_classes_label = QtWidgets.QLabel(self.tab)
        self.number_of_classes_label.setGeometry(QtCore.QRect(30, 120, 171, 16))
        self.number_of_classes_label.setObjectName("number_of_classes_label")
        self.number_of_classes = QtWidgets.QSpinBox(self.tab)
        self.number_of_classes.setGeometry(QtCore.QRect(30, 140, 231, 22))
        self.number_of_classes.setMinimum(1)
        self.number_of_classes.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.number_of_classes.setObjectName("number_of_classes")
        self.coefficient_of_mean_value = QtWidgets.QDoubleSpinBox(self.tab)
        self.coefficient_of_mean_value.setGeometry(QtCore.QRect(30, 310, 231, 22))
        self.coefficient_of_mean_value.setSingleStep(0.1)
        self.coefficient_of_mean_value.setObjectName("coefficient_of_mean_value")
        self.coefficient_of_varience = QtWidgets.QDoubleSpinBox(self.tab)
        self.coefficient_of_varience.setGeometry(QtCore.QRect(30, 370, 231, 22))
        self.coefficient_of_varience.setSingleStep(0.1)
        self.coefficient_of_varience.setObjectName("coefficient_of_varience")
        self.coefficient_of_mean_value_label = QtWidgets.QLabel(self.tab)
        self.coefficient_of_mean_value_label.setGeometry(QtCore.QRect(30, 290, 171, 16))
        self.coefficient_of_mean_value_label.setObjectName("coefficient_of_mean_value_label")
        self.coefficient_of_varience_label = QtWidgets.QLabel(self.tab)
        self.coefficient_of_varience_label.setGeometry(QtCore.QRect(30, 340, 171, 16))
        self.coefficient_of_varience_label.setObjectName("coefficient_of_varience_label")
        self.number_of_features_label = QtWidgets.QLabel(self.tab)
        self.number_of_features_label.setGeometry(QtCore.QRect(30, 170, 171, 16))
        self.number_of_features_label.setObjectName("number_of_features_label")
        self.number_of_features = QtWidgets.QSpinBox(self.tab)
        self.number_of_features.setGeometry(QtCore.QRect(30, 190, 231, 22))
        self.number_of_features.setMinimum(2)
        self.number_of_features.setMaximum(1000)
        self.number_of_features.setSingleStep(1)
        self.number_of_features.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.number_of_features.setObjectName("number_of_features")
        self.number_of_each_class_label = QtWidgets.QLabel(self.tab)
        self.number_of_each_class_label.setGeometry(QtCore.QRect(30, 230, 231, 16))
        self.number_of_each_class_label.setObjectName("number_of_each_class_label")
        self.number_of_each_class = QtWidgets.QSpinBox(self.tab)
        self.number_of_each_class.setGeometry(QtCore.QRect(30, 250, 231, 22))
        self.number_of_each_class.setMinimum(1)
        self.number_of_each_class.setMaximum(1000)
        self.number_of_each_class.setSingleStep(10)
        self.number_of_each_class.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.number_of_each_class.setObjectName("number_of_each_class")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(30, 280, 231, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(30, 390, 231, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(30, 100, 231, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "2020214251-蔡景宜"))
        self.pushButton.setText(_translate("Form", "example PCA"))
        self.explained_varience.setText(_translate("Form", "explained variance:"))
        self.explained_varience_ratio.setText(_translate("Form", "explained variance ratio:"))
        self.noise_variance.setText(_translate("Form", "noise variance:"))
        self.n_components.setText(_translate("Form", "n components:"))
        self.rand.setText(_translate("Form", "rand PCA"))
        self.before_PCA.setText(_translate("Form", "before PCA:"))
        self.after_PCA.setText(_translate("Form", "after PCA:"))
        self.number_of_classes_label.setText(_translate("Form", "number of classes"))
        self.coefficient_of_mean_value_label.setText(_translate("Form", "coefficient of mean value"))
        self.coefficient_of_varience_label.setText(_translate("Form", "coefficient of varience"))
        self.number_of_features_label.setText(_translate("Form", "number of feture"))
        self.number_of_each_class_label.setText(_translate("Form", "number of sample（each class）"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))