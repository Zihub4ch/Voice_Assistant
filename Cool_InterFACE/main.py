from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("VA.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def on_click():
    print("Clicked!!!")

form.pushButton.clicked.connect(on_click)


app.exec()