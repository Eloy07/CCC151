# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgStudentUpdated.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgStudentUpdated(object): 
    def setupUi(self, dlgStudentAdded):
        dlgStudentAdded.setObjectName("dlgStudentAdded")
        dlgStudentAdded.resize(202, 147)
        dlgStudentAdded.setMinimumSize(QtCore.QSize(202, 147))
        dlgStudentAdded.setMaximumSize(QtCore.QSize(202, 147))
        dlgStudentAdded.setStyleSheet("background: #1b2023;")
        self.btnStudentUpdated = QtWidgets.QPushButton(dlgStudentAdded)
        self.btnStudentUpdated.setGeometry(QtCore.QRect(60, 100, 75, 23))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(9)
        self.btnStudentUpdated.setFont(font)
        self.btnStudentUpdated.setStyleSheet("background: white;\n"
"")
        self.btnStudentUpdated.setObjectName("btnStudentUpdated")
        self.txtStudentUpdated = QtWidgets.QLabel(dlgStudentAdded)
        self.txtStudentUpdated.setGeometry(QtCore.QRect(20, 10, 171, 81))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txtStudentUpdated.setFont(font)
        self.txtStudentUpdated.setStyleSheet("color: #c3bcc2;")
        self.txtStudentUpdated.setObjectName("txtStudentUpdated")

        self.retranslateUi(dlgStudentAdded)
        QtCore.QMetaObject.connectSlotsByName(dlgStudentAdded)

    def retranslateUi(self, dlgStudentAdded):
        _translate = QtCore.QCoreApplication.translate
        dlgStudentAdded.setWindowTitle(_translate("dlgStudentAdded", "Student Added"))
        self.btnStudentUpdated.setText(_translate("dlgStudentAdded", "Ok"))
        self.txtStudentUpdated.setText(_translate("dlgStudentAdded", "Student Updated"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgStudentAdded = QtWidgets.QDialog()
    ui = Ui_dlgStudentAdded()
    ui.setupUi(dlgStudentAdded)
    dlgStudentAdded.show()
    sys.exit(app.exec_())
