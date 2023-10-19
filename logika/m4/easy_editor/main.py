from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap 

from PIL import Image, ImageFilter

import os


add = QApplication([])
window = QWidget()

btn_folder=QPushButton("Папка")
btn_left= QPushButton("Ліворуч")
btn_right= QPushButton("Параворуч")
btn_zerk = QPushButton("Дзеркало")
btn_rizk= QPushButton("Різкість")
btn_b_w= QPushButton("Ч/Б")

lst_files = QListWidget()

lb_kart = QLabel('Картинка')

line_base = QHBoxLayout()

line2 = QVBoxLayout()

line3 = QHBoxLayout()

line4 = QVBoxLayout()


line4.addWidget(btn_folder)
line4.addWidget(lst_files)

line3.addWidget(btn_left)
line3.addWidget(btn_right)
line3.addWidget(btn_zerk)
line3.addWidget(btn_rizk)
line3.addWidget(btn_b_w)

line2.addWidget(lb_kart)

line2.addLayout(line3)
line_base.addLayout(line4 , 1)
line_base.addLayout(line2 , 4)

workdir = QFileDialog.getExistingDirectory()

print(workdir)

files = os.listdir(workdir)
print(files)

def filter(filenames):
    result = []
    ext = ['jpg', ' png', 'jpeg', 'bmp', 'gif']

    for file in filenames:
        #print(file.split('.'))
        #print(file.split('.')[-1])
        if file.split('.')[-1] in ext:
            result.append(file)

    return result

print(filter(files))
window.setLayout(line_base)


window.show()
add.exec_()