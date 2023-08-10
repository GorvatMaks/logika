from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton

app = QApplication([])
main_win = QWidget()

label = QLabel("Коли я почав вчити програмування?")

knopka_gg1 = QRadioButton("1939")
knopka_gg2 = QRadioButton("1954")
knopka_gg3 = QRadioButton("2001")
knopka_gg4 = QRadioButton("2022")

hura = QVBoxLayout()
vova_1 = QHBoxLayout()
vova_2 = QHBoxLayout()
vova_3 = QHBoxLayout()

vova_1.addWidget(label, alignment=Qt.AlignCenter)
vova_2.addWidget(knopka_gg1, alignment=Qt.AlignCenter)
vova_2.addWidget(knopka_gg2, alignment=Qt.AlignCenter)
vova_3.addWidget(knopka_gg3, alignment=Qt.AlignCenter)
vova_3.addWidget(knopka_gg4, alignment=Qt.AlignCenter)

hura.addLayout(vova_1)
hura.addLayout(vova_2)
hura.addLayout(vova_3)



main_win.setLayout(hura)

main_win.show()
app.exec_()