from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap 

from PIL import Image, ImageFilter

import os


add = QApplication([])
window = QWidget()

#btn_coler=QPushButton("Зміна Дезайну на ч\б")
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


#line4.addWidget(btn_coler)
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




def filter(filenames):
    result = []
    ext = ['jpg', ' png', 'jpeg', 'bmp', 'gif']

    for file in filenames:
        #print(file.split('.'))
        #print(file.split('.')[-1])
        if file.split('.')[-1] in ext:
            result.append(file)

    return result

#print(filter(files))

def showFiles():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    files = os.listdir(workdir)

    graphic = filter(files)

    lst_files.clear()
    lst_files.addItems(graphic)

class ImageProcessor():
    def __init__(self):
        self.original = None
        self.filename = None
        self.save_dir = 'Modified/'
    
    def load_image(self, filename):
        self.filename = filename

        full_path = os.path.join(workdir , filename)

        self.original = Image.open(full_path)

    def show_image(self, path):
        lb_kart.hide()

        pixmapimage = QPixmap(path)
        w, h = lb_kart.width(), lb_kart.height()
        pixmapimage = pixmapimage.scaled(w , h, Qt.KeepAspectRatio)

        lb_kart.setPixmap(pixmapimage)

        lb_kart.show()

    def saveAndShowImage(self):
        path = os.path.join(workdir, self.save_dir)

        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        
        image_path = os.path.join(path , self.filename )
       
        self.original.save(image_path)
        self.show_image(image_path)
        
    def do_bw(self):
        self.original = self.original.convert("L")
        self.saveAndShowImage()

    def do_left(self):
        self.original = self.original.transpose(Image.ROTATE_90)
        self.saveAndShowImage()

    def do_right(self):
        self.original = self.original.transpose(Image.ROTATE_270)
        self.saveAndShowImage()

    def do_flip(self):
        self.original = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveAndShowImage()

    def do_sharp(self):
        self.original = self.original.filter(ImageFilter.SHARPEN)
        self.saveAndShowImage()



def showChosenItem():
    filename = lst_files.currentItem().text()
    workimage.load_image(filename)
    
    full_path = os.path.join(workdir , filename)
    workimage.show_image(full_path)


workimage = ImageProcessor()

lst_files.currentRowChanged.connect(showChosenItem)

btn_folder.clicked.connect(showFiles)

btn_b_w.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_rizk.clicked.connect(workimage.do_sharp)
btn_zerk.clicked.connect(workimage.do_flip)




window.setLayout(line_base)


window.show()
add.exec_()