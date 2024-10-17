import sys 
from PyQt6.QtWidgets import * 


class InputBar(QWidget):
    def __init__(self):

        super().__init__()
        self.Window1()
    
    def Window1(self):
        self.setWindowTitle("MY Browser")
        self.layout=QHBoxLayout()
        # self.resize(400, 200) 
        self.button=QPushButton("enter")
        self.layout.addWidget(self.button)
        self.line_edit=QLineEdit()
        self.layout.addWidget(self.line_edit)
        self.layout.addStretch()
        self.setLayout(self.layout)
    
class   MyWindow(QWidget):
    def __init__(self):
        super().__init__() 
        self.showWindow()
    def showWindow(self):
        self.inptBar=InputBar() 
        self.layout=QVBoxLayout()
        self.layout.addWidget(self.inptBar)
        self.layout.addStretch()
        self.setLayout(self.layout)




if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWindow()
    window.showMaximized()
    sys.exit(app.exec())