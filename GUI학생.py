import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    #####

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        vbox = QVBoxLayout()

        # 1
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        self.lbl1 = QLabel('Name:')
        self.lbl2 = QLineEdit()
        hbox1.addWidget(self.lbl1)
        hbox1.addWidget(self.lbl2)
        self.lbl3 = QLabel('Age:')
        self.lbl4 = QLineEdit()
        hbox1.addWidget(self.lbl3)
        hbox1.addWidget(self.lbl4)
        self.lbl5 = QLabel('Score:')
        self.lbl6 = QLineEdit()
        hbox1.addWidget(self.lbl5)
        hbox1.addWidget(self.lbl6)

        # 2
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        self.lbl7 = QLabel('Amount:')
        self.lbl8 = QLineEdit()
        hbox2.addWidget(self.lbl7)
        hbox2.addWidget(self.lbl8)
        self.lbl9 = QLabel('Key:')
        self.lbl10 = QComboBox()
        self.lbl10.addItem('Name')
        self.lbl10.addItem('Age')
        self.lbl10.addItem('Score')
        hbox2.addWidget(self.lbl9)
        hbox2.addWidget(self.lbl10)

        # 3
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        self.lbl11 = QPushButton('Add')
        self.lbl11.clicked.connect(self.Add)
        self.lbl12 = QPushButton('Del')
        self.lbl12.clicked.connect(self.S_Del)
        self.lbl13 = QPushButton('Find')
        self.lbl13.clicked.connect(self.S_Find)
        self.lbl14 = QPushButton('Inc')
        self.lbl14.clicked.connect(self.S_Inc)
        self.lbl15 = QPushButton('Show')
        self.lbl15.clicked.connect(self.Show)
        hbox3.addWidget(self.lbl11)
        hbox3.addWidget(self.lbl12)
        hbox3.addWidget(self.lbl13)
        hbox3.addWidget(self.lbl14)
        hbox3.addWidget(self.lbl15)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        # 4
        self.lbl16 = QLabel('Result:')

        # 5
        self.lbl17 = QTextEdit()

        vbox.addWidget(self.lbl16)
        vbox.addWidget(self.lbl17)

        self.setLayout(vbox)
        self.show()

    def showdb(self, keyname):
        temptext = ""
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                temptext += attr + "=" + str(p[attr]) + ' '
            temptext += '\n'
        self.lbl17.setText(temptext)

    # Add

    def Add(self):
        nametext = self.lbl2.text()
        if nametext == "":
            nametext = "None"
        agetext = self.lbl4.text()
        if agetext == "":
            agetext = 0
        scoretext = self.lbl6.text()
        if scoretext == "":
            scoretext = 0
        try:
            self.scoredb.append({"Name": nametext, "Age": int(agetext), "Score": int(scoretext)})
        except ValueError:
            self.lbl17.setText("Wrong Type")
        else:
            self.showdb('Name')

    # Del

    def Del(self, name):
        for p in sorted(self.scoredb, key=lambda person: person['Name']):
            if p['Name'] == name:
                self.scoredb.remove(p)
        self.showdb('Name')

    def S_Del(self):
        self.Del(self.lbl2.text())

    # Find

    def Find(self, name):
        temptext = ""
        for p in sorted(self.scoredb, key=lambda person: person['Name']):
            if p['Name'] == name:
                for attr in sorted(p):
                    temptext += attr + "=" + str(p[attr]) + ' '
        temptext += '\n'
        self.lbl17.setText(temptext)

    def S_Find(self):
        self.Find(self.lbl2.text())

    # Inc

    def Inc(self, name, amount):
        amt = int(amount)
        for p in self.scoredb:
            if p['Name'] == name:
                p['Score'] = str(int(p['Score']) + amt)

        self.showdb('Name')

    def S_Inc(self):
        self.Inc(self.lbl2.text(), self.lbl8.text())

    # Show

    def Show(self):
        self.showdb(self.lbl10.currentText())

    #####

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_()) 