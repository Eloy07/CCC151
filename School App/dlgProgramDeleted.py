# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgProgramDeleted.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgProgramDeleted(object):
    def setupUi(self, dlgProgramDeleted):
        dlgProgramDeleted.setObjectName("dlgProgramDeleted")
        dlgProgramDeleted.resize(202, 147)
        dlgProgramDeleted.setMinimumSize(QtCore.QSize(202, 147))
        dlgProgramDeleted.setMaximumSize(QtCore.QSize(202, 147))
        dlgProgramDeleted.setStyleSheet("background: #1b2023;")
        self.txtPorgramDeleted = QtWidgets.QLabel(dlgProgramDeleted)
        self.txtPorgramDeleted.setGeometry(QtCore.QRect(20, 10, 181, 81))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txtPorgramDeleted.setFont(font)
        self.txtPorgramDeleted.setStyleSheet("color: #c3bcc2;")
        self.txtPorgramDeleted.setObjectName("txtPorgramDeleted")
        self.btnDlgProgramDeleted = QtWidgets.QPushButton(dlgProgramDeleted)
        self.btnDlgProgramDeleted.setGeometry(QtCore.QRect(60, 100, 75, 23))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(9)
        self.btnDlgProgramDeleted.setFont(font)
        self.btnDlgProgramDeleted.setStyleSheet("background: white;\n"
"")
        self.btnDlgProgramDeleted.setObjectName("btnDlgProgramDeleted")

        self.retranslateUi(dlgProgramDeleted)
        QtCore.QMetaObject.connectSlotsByName(dlgProgramDeleted)

    def retranslateUi(self, dlgProgramDeleted):
        _translate = QtCore.QCoreApplication.translate
        dlgProgramDeleted.setWindowTitle(_translate("dlgProgramDeleted", "Porgram Deleted"))
        self.txtPorgramDeleted.setText(_translate("dlgProgramDeleted", "Program Deleted"))
        self.btnDlgProgramDeleted.setText(_translate("dlgProgramDeleted", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgProgramDeleted = QtWidgets.QDialog()
    ui = Ui_dlgProgramDeleted()
    ui.setupUi(dlgProgramDeleted)
    dlgProgramDeleted.show()
    sys.exit(app.exec_())
