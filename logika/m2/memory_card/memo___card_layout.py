''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)



btm_menu = QPushButton("Меню")

btn_sleep = QPushButton("Відпочити")

btn_Ok = QPushButton("Відповісти")

lb_Question = QLabel('')

box_minutes = QPushButton()
box_minutes.setValue(5)

RadioGroupBox = QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup()

rbtn_1 = QRadioButton("")
rbtn_2 = QRadioButton("")
rbtn_3 = QRadioButton("")
rbtn_4 = QRadioButton("")

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox("Результат")
lb_Result = QLabel('')
lb_Correct = QLabel('')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, aligament=(Qt.Alignleft | Qt.AlignTop))
layout_res.addWidget(lb_Result, aligament=(Qt.AlignHCenter ))
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

def show_result():
    ''' показати панель відповідей '''
    pass

def show_question():
    ''' показати панель запитань '''
    pass