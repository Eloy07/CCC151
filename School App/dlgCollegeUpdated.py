# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgCollegeUpdated.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgCollegeUpdated(object):
    def setupUi(self, dlgCollegeUpdated):
        dlgCollegeUpdated.setObjectName("dlgCollegeUpdated")
        dlgCollegeUpdated.resize(202, 147)
        dlgCollegeUpdated.setMinimumSize(QtCore.QSize(202, 147))
        dlgCollegeUpdated.setMaximumSize(QtCore.QSize(202, 147))
        dlgCollegeUpdated.setStyleSheet("background: #1b2023;")
        self.btnCollegeUpdated = QtWidgets.QPushButton(dlgCollegeUpdated)
        self.btnCollegeUpdated.setGeometry(QtCore.QRect(60, 100, 75, 23))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(9)
        self.btnCollegeUpdated.setFont(font)
        self.btnCollegeUpdated.setStyleSheet("background: white;\n"
"")
        self.btnCollegeUpdated.setObjectName("btnCollegeUpdated")
        self.txtCollegeUpdated = QtWidgets.QLabel(dlgCollegeUpdated)
        self.txtCollegeUpdated.setGeometry(QtCore.QRect(20, 10, 171, 81))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txtCollegeUpdated.setFont(font)
        self.txtCollegeUpdated.setStyleSheet("color: #c3bcc2;")
        self.txtCollegeUpdated.setObjectName("txtCollegeUpdated")

        self.retranslateUi(dlgCollegeUpdated)
        QtCore.QMetaObject.connectSlotsByName(dlgCollegeUpdated)

    def retranslateUi(self, dlgCollegeUpdated):
        _translate = QtCore.QCoreApplication.translate
        dlgCollegeUpdated.setWindowTitle(_translate("dlgCollegeUpdated", "Student Added"))
        self.btnCollegeUpdated.setText(_translate("dlgCollegeUpdated", "Ok"))
        self.txtCollegeUpdated.setText(_translate("dlgCollegeUpdated", "College Updated"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgCollegeUpdated = QtWidgets.QDialog()
    ui = Ui_dlgCollegeUpdated()
    ui.setupUi(dlgCollegeUpdated)
    dlgCollegeUpdated.show()
    sys.exit(app.exec_())
