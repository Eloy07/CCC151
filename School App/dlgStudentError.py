# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgStudentError.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgStudentError(object):
    def setupUi(self, dlgStudentError):
        dlgStudentError.setObjectName("dlgStudentError")
        dlgStudentError.resize(202, 147)
        dlgStudentError.setMinimumSize(QtCore.QSize(202, 147))
        dlgStudentError.setMaximumSize(QtCore.QSize(202, 147))
        dlgStudentError.setStyleSheet("background: #1b2023;")
        self.txtStudentError = QtWidgets.QLabel(dlgStudentError)
        self.txtStudentError.setGeometry(QtCore.QRect(40, 20, 131, 81))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtStudentError.setFont(font)
        self.txtStudentError.setStyleSheet("color: #c3bcc2;")
        self.txtStudentError.setObjectName("txtStudentError")
        self.btnDlgStudentError = QtWidgets.QPushButton(dlgStudentError)
        self.btnDlgStudentError.setGeometry(QtCore.QRect(60, 110, 75, 23))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(9)
        self.btnDlgStudentError.setFont(font)
        self.btnDlgStudentError.setStyleSheet("background: white;\n"
"")
        self.btnDlgStudentError.setObjectName("btnDlgStudentError")

        self.retranslateUi(dlgStudentError)
        QtCore.QMetaObject.connectSlotsByName(dlgStudentError)

    def retranslateUi(self, dlgStudentError):
        _translate = QtCore.QCoreApplication.translate
        dlgStudentError.setWindowTitle(_translate("dlgStudentError", "Error"))
        self.txtStudentError.setText(_translate("dlgStudentError", "All blanks must \n"
" be filled in"))
        self.btnDlgStudentError.setText(_translate("dlgStudentError", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgStudentError = QtWidgets.QDialog()
    ui = Ui_dlgStudentError()
    ui.setupUi(dlgStudentError)
    dlgStudentError.show()
    sys.exit(app.exec_())
