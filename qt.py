
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QRadioButton, QVBoxLayout,
    QMessageBox
)

def send():
    name = entry_name.text()
    age = entry_age.text()
    gender = "Мужской" if male.isChecked() else "Женский"

    if name == "" or not age.isdigit():
        QMessageBox.warning(window, "Ошибка")
    else:
        result.setText(f"{name}, {age} лет, {gender}")
        QMessageBox.information(window, "Готово")


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Анкета")
window.resize(567, 765)


name = QLabel("Ваше имя:")
entry_name = QLineEdit()


age = QLabel("Ваш возраст:")
entry_age = QLineEdit()


gender = QLabel("Ваш пол:")

male = QRadioButton("Мужской")
female = QRadioButton("Женский")
male.setChecked(True)


button = QPushButton("Отправить")
button.clicked.connect(send)


result = QLabel("Результат:")

layout = QVBoxLayout()

layout.addWidget(name)
layout.addWidget(entry_name)

layout.addWidget(age)
layout.addWidget(entry_age)

layout.addWidget(gender)
layout.addWidget(male)
layout.addWidget(female)

layout.addWidget(button)
layout.addWidget(result)

window.setLayout(layout)

window.show()
sys.exit(app.exec())
