# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo5.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(982, 1009)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_1_horizontalLayout = QtWidgets.QHBoxLayout()
        self.main_1_horizontalLayout.setObjectName("main_1_horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.main_1_horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.main_1_horizontalLayout)
        self.main_2_horizontalLayout = QtWidgets.QHBoxLayout()
        self.main_2_horizontalLayout.setSpacing(0)
        self.main_2_horizontalLayout.setObjectName("main_2_horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(190, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.main_2_horizontalLayout.addItem(spacerItem1)
        self.left_widget = QtWidgets.QWidget(Form)
        self.left_widget.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.left_widget.setObjectName("left_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.main_2_horizontalLayout.addWidget(self.left_widget)
        self.main_widget = QtWidgets.QWidget(Form)
        self.main_widget.setStyleSheet("background-color:  rgb(11,11,11);")
        self.main_widget.setObjectName("main_widget")
        self.main_grid_Layout = QtWidgets.QGridLayout(self.main_widget)
        self.main_grid_Layout.setContentsMargins(9, 9, 9, 9)
        self.main_grid_Layout.setObjectName("main_grid_Layout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.main_grid_Layout.addItem(spacerItem2, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(5, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 0, 2, 1, 1)
        self.mange_widget = QtWidgets.QWidget(self.main_widget)
        self.mange_widget.setStyleSheet("background-color: rgb(11,11,11);")
        self.mange_widget.setObjectName("mange_widget")
        self.gridLayout_4.addWidget(self.mange_widget, 1, 2, 1, 1)
        self.main_widget_2 = QtWidgets.QWidget(self.main_widget)
        self.main_widget_2.setStyleSheet("\n"
"background-color: rgb(11,11,11);")
        self.main_widget_2.setObjectName("main_widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.main_widget_2)
        self.widget.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.gridLayout_4.addWidget(self.main_widget_2, 0, 0, 1, 1)
        self.main_grid_Layout.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.main_2_horizontalLayout.addWidget(self.main_widget)
        self.verticalLayout.addLayout(self.main_2_horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
