Widget
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
import sys

class MyWindow(QtWidget):
	def __init__(self):
		super (MyWindow, self).__init__()
		self.initGUI()

def initGUI(self):
	self.setWindowTitle('A First Window')
	# a button 
	self.mybutton = QPushButton(self)
	self.mybutton.setText("Oks")
	# A text field
	self.mytext = QLineEdit(self)
	self.mytext.setText("Welcome")
	# An image
	filepath = "media/qt-loop.png" # relative path of your image file
	self.mypixmap = QPixmap(filepath)
	self.myimg = QLabel(self)
	self.myimg.setPix.map(self.mypixmap)

	#Set up the window and arrange all the widgets
	pixrect = self.mypixmap.rect()
	self.setGeometry(10, 10, pixrect.width(), pixrect.height() + 50)
	self.mytext.move(20, pixrect.height() + 20)
	self.mybutton.move(150, pixrect.height() + 15)
	self.show()

if  __name__ == "__main__" :

	app = QApplication(sys.argv)
	Mywindow1 = MyWindow()
	Mywindow2 = MyWindow()
	Mywindow2.move(20, 500)
	sys.exit(app.exec_()) # start the event loop