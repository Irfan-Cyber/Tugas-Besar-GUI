# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataTransaksi.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(696, 480)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 701, 101))
        self.label.setStyleSheet("background-color: #647381;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 111, 101))
        self.label_2.setStyleSheet("image: url(:/newPrefix/images__1_-removebg-preview.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 40, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(270, 120, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 110, 491, 351))
        self.label_5.setStyleSheet("background: #647381;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(120, 140, 451, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.table_dataTransaksi = QtWidgets.QTableWidget(Dialog)
        self.table_dataTransaksi.setGeometry(QtCore.QRect(120, 160, 451, 251))
        self.table_dataTransaksi.setFrameShape(QtWidgets.QFrame.Box)
        self.table_dataTransaksi.setFrameShadow(QtWidgets.QFrame.Plain)
        self.table_dataTransaksi.setLineWidth(2)
        self.table_dataTransaksi.setRowCount(1000)
        self.table_dataTransaksi.setColumnCount(4)
        self.table_dataTransaksi.setObjectName("table_dataTransaksi")
        item = QtWidgets.QTableWidgetItem()
        self.table_dataTransaksi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dataTransaksi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dataTransaksi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dataTransaksi.setHorizontalHeaderItem(3, item)
        self.table_dataTransaksi.horizontalHeader().setDefaultSectionSize(150)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(290, 120, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.PB_kembali3 = QtWidgets.QPushButton(Dialog)
        self.PB_kembali3.setGeometry(QtCore.QRect(120, 420, 451, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PB_kembali3.setFont(font)
        self.PB_kembali3.setObjectName("PB_kembali3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.getData()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Transaksi"))
        self.label_4.setText(_translate("Dialog", "Data Transaksi"))
        item = self.table_dataTransaksi.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID Customer"))
        item = self.table_dataTransaksi.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Customer"))
        item = self.table_dataTransaksi.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Jumlah Barang"))
        item = self.table_dataTransaksi.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Total Bayar"))
        self.label_6.setText(_translate("Dialog", "Data Transaksi"))
        self.PB_kembali3.setText(_translate("Dialog", "KEMBALI"))\
       


    def getData(self):
        import connector
        cursor = connector.cnx.cursor()

        query = ("SELECT * FROM transaksi")
        cursor.execute(query)
        results = cursor.fetchall()
        i = 0
        for data in results:
            self.table_dataTransaksi.setItem(i,0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.table_dataTransaksi.setItem(i,1, QtWidgets.QTableWidgetItem(data[1]))
            self.table_dataTransaksi.setItem(i,2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.table_dataTransaksi.setItem(i,3, QtWidgets.QTableWidgetItem(str(data[3])))
            i = i + 1
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
