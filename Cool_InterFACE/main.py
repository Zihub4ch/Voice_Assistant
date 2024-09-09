from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from AW import AnotherWindow1

Form, Window = uic.loadUiType("VA.ui")
Form1, AnotherWindow1 = uic.loadUiType("AW.ui")

app = QApplication([])
window = Window()
window_2 = AnotherWindow1()
form = Form()
form1 = Form1()
form.setupUi(window)
form1.setupUi(window_2)
window.show()


def show_MainWindow(self):
    self.ui.pushButton_3.clicked.connect(show_AnotherWindow)
    self.ui.pushButton_3.clicked.connect(self.close)


def show_AnotherWindow(self, checked):
    self.w.show()

form.pushButton_3.clicked.connect(show_MainWindow)

app.exec()