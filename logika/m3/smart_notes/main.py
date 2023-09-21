from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json 

app =  QApplication([])

window = QWidget()


field_text = QTextEdit()
Ib_notes = QLabel(" Сптсок заміток")
lst_notes = QListWidget()

btn_note_crete = QPushButton('Створити_note')
btn_note_delete = QPushButton('Видалити_note')
btn_note_save = QPushButton('Зберегти_note')

Ib_tag = QLabel(" Список тегів")
list_teg = QListWidget()

btn_note_add_teg = QPushButton('Добавити_teg')
btn_note_unf_teg = QPushButton('Відкріпити_teg')
btn_note_scr_teg = QPushButton('Пошук_teg')

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

layout_notes.addLayout(col1)
layout_notes.addLayout(col2)

col1.addWidget(field_text)

col2.addWidget(Ib_notes)
col2.addWidget(lst_notes)

row1 = QHBoxLayout()
row1.addWidget(btn_note_crete)
row1.addWidget(btn_note_delete)
row1.addWidget(btn_note_save)

row2 = QVBoxLayout()
row2.addWidget(btn_note_add_teg)
row2.addWidget(btn_note_unf_teg)
row2.addWidget(btn_note_scr_teg)
row2.addWidget(Ib_tag)
row2.addWidget(list_teg)

col2.addLayout(row2)
col2.addLayout(row1)
#НАЗАР КУ




with open('note.json', 'r', encoding='utf-8') as file:
    notes = json.load(file)

lst_notes.addItems(notes)






window.setLayout(layout_notes)
window.show()
app.exec_()