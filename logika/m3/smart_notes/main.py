from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json 

def writeToFile():
    with open('note.json', 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, sort_keys=True, indent=4)
        
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

field_text1 = QLineEdit("")
btn_note_add_teg = QPushButton('Добавити_teg')
btn_note_unf_teg = QPushButton('Відкріпити_teg')
btn_note_scr_teg = QPushButton('Пошук за тегом')

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2, stretch=1)

col1.addWidget(field_text)

col2.addWidget(Ib_notes)
col2.addWidget(lst_notes)

row1 = QHBoxLayout()
row1.addWidget(btn_note_add_teg)
row1.addWidget(btn_note_unf_teg)
row1.addWidget(btn_note_scr_teg)


row2 = QHBoxLayout()
row2.addWidget(btn_note_crete)
row2.addWidget(btn_note_delete)
row2.addWidget(btn_note_save)

col2.addLayout(row2)
col2.addWidget(Ib_tag)
col2.addWidget(list_teg)
col2.addWidget(field_text1)
col2.addLayout(row1)
#НАЗАР КУ




with open('note.json', 'r', encoding='utf-8') as file:
    notes = json.load(file)


def show_note():
    key = lst_notes.currentItem().text()

    field_text.setText(notes[key]['текст'])

    list_teg.clear()
    list_teg.addItems(notes[key]['теги'])

def add_note():
    note_name, ok = QInputDialog.getText(window, 'Узбетьська шаурма', 'назва шаурми')

    if note_name and ok:
        notes[note_name] = {"текст": "","теги": []}
        lst_notes.addItem(note_name)

def seve_note():
    if lst_notes.currentItem().text():
        key = lst_notes.currentItem().text()
        notes[key]['текст'] = field_text.toPlainText()


        writeToFile()
        

def del_note():
    if lst_notes.currentItem().text():
        key = lst_notes.currentItem().text()
        del notes[key]

        field_text.clear()
        list_teg.clear()
        lst_notes.clear()

        lst_notes.addItems(notes)
        writeToFile()

def add_teg():
    key = lst_notes.currentItem().text()
    
    teg_input = field_text1.text()

    notes[key]['теги'].append(teg_input)

    list_teg.addItem(teg_input)
    writeToFile()

def del_teg():
    key = lst_notes.currentItem().text()
    lis_teg = list_teg.currentItem().text()

    notes[key]['теги'].remove(lis_teg)
    list_teg.clear()
    
    list_teg.addItems(notes[key]['теги'])
    writeToFile()

def serch_teg():
    tag = field_text1.text()

    if btn_note_scr_teg.text() == 'Пошук за тегом':
        filter_notes = {}

        for key in notes:
            if tag in notes[key]['теги']:
                filter_notes[key] = notes[key]
       
        btn_note_scr_teg.setText('Скинути пошук')
        
        lst_notes.clear()
        lst_notes.addItems(filter_notes)


        list_teg.clear()

    elif btn_note_scr_teg.text() =='Скинути пошук':
        btn_note_scr_teg.setText('Пошук за тегом')
        
        field_text.clear()
        lst_notes.clear()
        list_teg.clear()
        field_text1.clear()

        lst_notes.addItems(notes)

btn_note_add_teg.clicked.connect(add_teg)
btn_note_unf_teg.clicked.connect(del_teg)
btn_note_scr_teg.clicked.connect(serch_teg)


lst_notes.itemClicked.connect(show_note)
btn_note_crete.clicked.connect(add_note)
btn_note_save.clicked.connect(seve_note)
btn_note_delete.clicked.connect(del_note)
lst_notes.addItems(notes)









window.setLayout(layout_notes)
window.show()
app.exec_()