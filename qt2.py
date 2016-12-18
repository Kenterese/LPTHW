from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
import sys

class MyWindow(QWidget):
    def _init_(self):
        super(MyWindow, self)._init_()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle('A First Window')
        # A button
        self.mybutton = QPushButton(self)
        self.mybutton.setText("Ok!")
        # A text field
        self.mytext = QLineEdit(self)
        self.mytext.setText("Welcome")
        # An image
        filepath = "media/1.png" # relative path of your image file
        self.mypixmap = QPixmap(filepath)
        self.myimg = QLabel(self)
        self.myimg.setPixmap(self.mypixmap)

        # Set up the window and arrange all the widgets
        pixrect = self.mypixmap.rect()
        self.setGeometry(10, 10, pixrect.width(), pixrect.height() + 50)
        self.mytext.move(20, pixrect.height() + 20)
        self.mybutton.move(150, pixrect.height() + 15)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv) # create the application
    mywindow1 = MyWindow() # create an instance of your window
    mywindow2 = MyWindow() # create an instance of your window
    mywindow2.move(20,500)
    sys.exit(app.exec_()) # start the event loop!