"""
gui01.py
The most basic Qt Program.
Opens an empty Window and moves it to the upper left corner of the screen.
"""

from PyQt5.QtWidgets import QApplication, QWidget
import sys

class MyWindow(QWidget):
    def _init_(self):
        super(MyWindow, self)._init_()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle('A First Window')
        self.resize(250,150)

if __name__ == "__main__":
    app = QApplication(sys.argv) # create the application
    mywindow = MyWindow() # create an instance of your window
    mywindow.move(0, 0)
    mywindow.show() # tell Qt to move your window visible
    sys.exit(app.exec_())# start the event input