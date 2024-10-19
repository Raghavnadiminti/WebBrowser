import sys 
from PyQt6.QtWidgets import * 
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtCore import *

class InputBar(QWidget):
    def __init__(self):

        super().__init__()
        self.Window1()
#//////////////////////////////////////////////   
    def Window1(self):
        self.setWindowTitle("MY Browser")
#------------------------------------------------
        self.mainlayout=QVBoxLayout()
        self.layout=QHBoxLayout()
         
        self.layout2=QVBoxLayout()
#------------------------------------------------
        self.button=QPushButton("enter")       
        self.line_edit=QLineEdit()
        self.button.clicked.connect(self.getinput) 
#---------------------------------------------------
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))  
        self.setStyleSheet("""
            
            QWebEngineView {
                border: 1px solid #ccc;
                border-radius: 5px;
                height:20000000px;
            }
        """)

#----------------------------------------------------    
        self.rightArrow=QPushButton(">")
        self.leftArrow=QPushButton("<")
        self.refresh=QPushButton("⟳")
        self.rightArrow.clicked.connect(self.browser.forward)
        self.leftArrow.clicked.connect(self.browser.back)
        self.refresh.clicked.connect(self.browser.reload)
#-------------------------------------------------------------
        self.layout2.setSpacing(0)
        self.layout2.setContentsMargins(0, 0, 0, 0)
        self.layout2.addWidget(self.browser)
        self.layout.addWidget(self.leftArrow)
        self.layout.addWidget(self.rightArrow)
        self.layout.addWidget(self.refresh)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.line_edit)
        # self.layout2.setStretch(0, 1)
       
#---------------------------------------------------------------
        self.mainlayout.addLayout(self.layout)
        self.mainlayout.addLayout(self.layout2)
          
        self.setLayout(self.mainlayout)
        # self.showMaximized()
#////////////////////////////////////////////////////////////////////       
    def getinput(self):
        input=self.line_edit.text()
        if input:
            self.browser.setUrl(QUrl(input))
    
    
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