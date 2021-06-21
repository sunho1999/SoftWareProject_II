from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


import random

class Button(QToolButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class Bingo(QWidget):



    def __init__(self, parent=None):
        super().__init__(parent)
        self.bingo_list = [] #좌표값이 들어가는 빙고리스트
        self.num = 0 #원빙고 투빙고 처럼 빙고 횟수

        #빙고 조건
        self.total = [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
        [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)],
        [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
        [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)],
        [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)],
        [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],
        [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)],
        [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
        [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)],
        [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)],
        [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)],
        [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]]
        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        #Digit Text
        self.digitButton = {}
        self.nansu = random.sample([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], 25)
        #이게 1~25 난수 생성리스트

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)


        textlayout = QGridLayout()
        newgamelayout = QGridLayout()

        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.startGame)
        newgamelayout.addWidget(self.newGameButton, 1, 1)


        #숫자패드 좌표값으로 임의의 숫자가 들어감

        cnt = 0
        for i in range(5):
            for j in range(5):
                self.digitButton[self.nansu[cnt]] = (i,j)
                textlayout.addWidget(Button(str(self.nansu[cnt]),self.buttonClicked),i,j)
                cnt +=1
        mainLayout.addLayout(textlayout,1,0)
        mainLayout.addLayout(newgamelayout,1,1)
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)
        self.message.setMaxLength(52)
        mainLayout.addWidget(self.message, 2, 0, 2, 2)




        self.setLayout(mainLayout)
        self.setWindowTitle("Bingo_game")
        # 숫자패드클릭
    def buttonClicked(self):
        self.game = True
        button = self.sender()
        self.bingo_list.append(self.digitButton[int(button.text())])

        self.bingoCheck(self.bingo_list)
        button.setText("X")
    #bingo check
    def bingoCheck(self, array):
        array.sort(key=lambda tup: tup[0])
        horizontal = [0, 0, 0, 0, 0]
        num = 0
        for i in array:
            if i[0] == 0:
                horizontal[0] += 1
            if i[0] == 1:
                horizontal[1] += 1
            if i[0] == 2:
                horizontal[2] += 1
            if i[0] == 3:
                horizontal[3] += 1
            if i[0] == 4:
                horizontal[4] += 1
        if horizontal[0] == 5:
            num += 1
        if horizontal[1] == 5:
            num += 1
        if horizontal[2] == 5:
            num += 1
        if horizontal[3] == 5:
            num += 1
        if horizontal[4] == 5:
            num += 1
        array.sort(key=lambda tup: tup[1])
        vertical = [0, 0, 0, 0, 0]
        for i in array:
            if i[1] == 0:
                vertical[0] += 1
            if i[1] == 1:
                vertical[1] += 1
            if i[1] == 2:
                vertical[2] += 1
            if i[1] == 3:
                vertical[3] += 1
            if i[1] == 4:
                vertical[4] += 1
        if vertical[0] == 5:
            num += 1
        if vertical[1] == 5:
            num += 1
        if vertical[2] == 5:
            num += 1
        if vertical[3] == 5:
            num += 1
        if vertical[4] == 5:
            num += 1

        if (0, 0) in array:
            if (1, 1) in array:
                if (2, 2) in array:
                    if (3, 3) in array:
                        if (4, 4) in array:
                            num += 1
        if (0, 4) in array:
            if (1, 3) in array:
                if (2, 2) in array:
                    if (3, 1) in array:
                        if (4, 0) in array:
                            num += 1
        if num ==5:
            self.message.setText("You win !!!!")
    #   New start
    def startGame(self):
        self.Bin = Bingo()
        self.__init__()
        Bin.show()
if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    Bin = Bingo()
    Bin.show()
    sys.exit(app.exec_())