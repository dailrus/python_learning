import design

import sys  
from PyQt5 import QtWidgets

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click_b1)
        self.pushButton_2.clicked.connect(self.A)

    def click_b1(self):
        self.pushButton.setText("1")
        self.pushButton_2.setText("0")

    def A(self):
        self.pushButton.setText("0")
        self.pushButton_2.setText("1")
        

def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = ExampleApp()  
    window.show()  
    app.exec_()  

if __name__ == '__main__':  
    main()
