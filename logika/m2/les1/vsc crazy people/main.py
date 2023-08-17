from PyQt5.QtCore import Qt
from PyQt5.QtCore import QtMsgType
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
main_window = QWidget()

button = QPushButton("Згенерувати")
text = QLabel("Натисни щоб дізнатися переможця")


line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winer, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)

winer = QLabel("?")

def win():
    ran = randint(1, 1000)
    winer.setText(str(ran))
    button.hide()

button.clicked.connect(win)    


main_window.setLayout(line)

main_window.show()
app.exec_()
