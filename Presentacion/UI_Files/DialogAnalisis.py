# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Presentacion/UI_Files/DialogAnalisis.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogAnalisis(object):
    def setupUi(self, DialogAnalisis):
        DialogAnalisis.setObjectName("DialogAnalisis")
        DialogAnalisis.resize(948, 490)
        DialogAnalisis.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.label = QtWidgets.QLabel(DialogAnalisis)
        self.label.setGeometry(QtCore.QRect(500, 20, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.btn_borrar_archivo = QtWidgets.QPushButton(DialogAnalisis)
        self.btn_borrar_archivo.setGeometry(QtCore.QRect(310, 60, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_borrar_archivo.setFont(font)
        self.btn_borrar_archivo.setStyleSheet("background-color: rgb(62, 134, 179);\n"
"color: rgb(255, 255, 255);")
        self.btn_borrar_archivo.setObjectName("btn_borrar_archivo")
        self.btn_analizar = QtWidgets.QPushButton(DialogAnalisis)
        self.btn_analizar.setGeometry(QtCore.QRect(310, 120, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_analizar.setFont(font)
        self.btn_analizar.setStyleSheet("background-color: rgb(62, 134, 179);\n"
"color: rgb(255, 255, 255);")
        self.btn_analizar.setObjectName("btn_analizar")
        self.label_2 = QtWidgets.QLabel(DialogAnalisis)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.listWidget_archivos = QtWidgets.QListWidget(DialogAnalisis)
        self.listWidget_archivos.setGeometry(QtCore.QRect(10, 60, 281, 191))
        self.listWidget_archivos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(15, 15, 15);")
        self.listWidget_archivos.setObjectName("listWidget_archivos")
        self.btn_guardar = QtWidgets.QPushButton(DialogAnalisis)
        self.btn_guardar.setGeometry(QtCore.QRect(30, 410, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_guardar.setFont(font)
        self.btn_guardar.setStyleSheet("background-color: rgb(62, 134, 179);\n"
"color: rgb(255, 255, 255);")
        self.btn_guardar.setObjectName("btn_guardar")
        self.btn_cancelar = QtWidgets.QPushButton(DialogAnalisis)
        self.btn_cancelar.setGeometry(QtCore.QRect(270, 410, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setStyleSheet("background-color: rgb(62, 134, 179);\n"
"color: rgb(255, 255, 255);")
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.comboBox_categorias = QtWidgets.QComboBox(DialogAnalisis)
        self.comboBox_categorias.setGeometry(QtCore.QRect(310, 220, 171, 32))
        self.comboBox_categorias.setStyleSheet("color: rgb(16, 16, 16);")
        self.comboBox_categorias.setObjectName("comboBox_categorias")
        self.label_3 = QtWidgets.QLabel(DialogAnalisis)
        self.label_3.setGeometry(QtCore.QRect(360, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.textEdit_preguntas = QtWidgets.QTextEdit(DialogAnalisis)
        self.textEdit_preguntas.setEnabled(True)
        self.textEdit_preguntas.setGeometry(QtCore.QRect(500, 50, 431, 421))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_preguntas.setFont(font)
        self.textEdit_preguntas.setStyleSheet("background-color: rgb(238, 238, 238);\n"
"color: rgb(7, 7, 7);")
        self.textEdit_preguntas.setReadOnly(True)
        self.textEdit_preguntas.setObjectName("textEdit_preguntas")
        self.label_4 = QtWidgets.QLabel(DialogAnalisis)
        self.label_4.setGeometry(QtCore.QRect(70, 320, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.lbl_total_preguntas = QtWidgets.QLabel(DialogAnalisis)
        self.lbl_total_preguntas.setGeometry(QtCore.QRect(270, 320, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lbl_total_preguntas.setFont(font)
        self.lbl_total_preguntas.setStyleSheet("color: rgb(0, 0, 0);")
        self.lbl_total_preguntas.setText("")
        self.lbl_total_preguntas.setObjectName("lbl_total_preguntas")

        self.retranslateUi(DialogAnalisis)
        QtCore.QMetaObject.connectSlotsByName(DialogAnalisis)

    def retranslateUi(self, DialogAnalisis):
        _translate = QtCore.QCoreApplication.translate
        DialogAnalisis.setWindowTitle(_translate("DialogAnalisis", "Dialog"))
        self.label.setText(_translate("DialogAnalisis", "Preguntas encontradas:"))
        self.btn_borrar_archivo.setText(_translate("DialogAnalisis", "Borrar archivo"))
        self.btn_analizar.setText(_translate("DialogAnalisis", "Analizar "))
        self.label_2.setText(_translate("DialogAnalisis", "Archivos"))
        self.btn_guardar.setText(_translate("DialogAnalisis", "Guardar preguntas"))
        self.btn_cancelar.setText(_translate("DialogAnalisis", "Cancelar"))
        self.label_3.setText(_translate("DialogAnalisis", "Categoria"))
        self.label_4.setText(_translate("DialogAnalisis", "Total preguntas: "))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogAnalisis = QtWidgets.QDialog()
    ui = Ui_DialogAnalisis()
    ui.setupUi(DialogAnalisis)
    DialogAnalisis.show()
    sys.exit(app.exec_())
