# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index5.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_Form(object):
    def setupUi(self, Form):

        # this will hide the title bar
        Form.setWindowFlag(Qt.FramelessWindowHint)

        Form.setObjectName("Form")
        Form.resize(839, 565)
        Form.setMinimumSize(QtCore.QSize(839, 565))
        Form.setMaximumSize(QtCore.QSize(839, 565))
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_gridLayout = QtWidgets.QGridLayout()
        self.top_gridLayout.setObjectName("top_gridLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("icon/wizard-004.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.top_gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.verticalLayout.addLayout(self.top_gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
import xyz_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
