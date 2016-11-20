from PyQt5.QtWidgets import QApplication, QtWidget
import sys

class MyWindow(QtWidget):
	def __init__(self):
		super (MyWindow, self).__init__()
		self.initGUI()

	def initGUI(self):
		self.setWindowTitle('A First Window')
resize(250, 150)

if __name__ == "__main__":
	app = QApplication(sys.argv) #create the application
	MyWindow = MyWindow() #create the instance of yout window
	mywindow.move(0,0)
	mywindow.show() # tell Qt to make your window viisble 
	sys.exit(app.exec_())  # startt the event loop