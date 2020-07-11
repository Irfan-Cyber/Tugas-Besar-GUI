# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import connector
import dashboard
import source_rc
import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(696, 480)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        Dialog.setFont(font)
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
        self.label_3.setGeometry(QtCore.QRect(110, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(110, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(100, 160, 491, 281))
        self.label_6.setStyleSheet("background: #647381;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(310, 130, 101, 71))
        self.label_5.setStyleSheet("image: url(:/newPrefix/Group 2.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(310, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.PB_login = QtWidgets.QPushButton(Dialog)
        self.PB_login.setGeometry(QtCore.QRect(220, 380, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.PB_login.setFont(font)
        self.PB_login.setStyleSheet("background: #AAB0B6;")
        self.PB_login.setObjectName("PB_login")
        self.LE_username = QtWidgets.QLineEdit(Dialog)
        self.LE_username.setGeometry(QtCore.QRect(200, 270, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LE_username.setFont(font)
        self.LE_username.setStyleSheet("background:transparent;\n"
"color:black;\n"
"border:none;\n"
"border-bottom:1px solid")
        self.LE_username.setObjectName("LE_username")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(140, 320, 51, 41))
        self.label_9.setStyleSheet("image: url(:/newPrefix/Group 4.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.LE_Password = QtWidgets.QLineEdit(Dialog)
        self.LE_Password.setGeometry(QtCore.QRect(200, 330, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LE_Password.setFont(font)
        self.LE_Password.setStyleSheet("background:transparent;\n"
"color:black;\n"
"border:none;\n"
"border-bottom:1px solid")
        self.LE_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LE_Password.setObjectName("LE_Password")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(140, 260, 51, 41))
        self.label_8.setStyleSheet("image: url(:/newPrefix/Group 3.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.PB_login.clicked.connect(self.doLogin)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Selamat Datang"))
        self.label_4.setText(_translate("Dialog", "Cafe MABAR"))
        self.label_7.setText(_translate("Dialog", "Admin"))
        self.PB_login.setText(_translate("Dialog", "Login"))
        self.LE_username.setPlaceholderText(_translate("Dialog", "Username"))
        self.LE_Password.setPlaceholderText(_translate("Dialog", "Password"))


    def doLogin(self):
        self.PB_login.setText("Loading")
        username = self.LE_username.text()
        password = self.LE_Password.text()
        cursor = connector.cnx.cursor()

        query = ("SELECT * FROM user WHERE username = %s AND password = %s")
        cursor.execute(query, (username, password))
        result = cursor.fetchall()
        if cursor.rowcount == 0:
            print("Tidak ada data")
        else:
            self.startDashboard()
            print("Data Ada")

        print(username)
        print(password)
        cursor.close()
    
    def startDashboard(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = dashboard.Dashboard()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
