
import sys 
from PyQt6.QtWidgets import * 
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtCore import * 
from MyBrowser import MyWindow
class Node():
    def __init__(self,b=None):
        self.data=MyWindow()
        self.next=b 
        self.prev=b
class Tabs():
    def __init__(self):
        self.head=None 
        self.last=None 
        
    def add(self,node):
        if self.head==None:
            self.head=node
            self.last=node 
            self.present=node 
        else:
            self.last.next=node 
            self.last=node  
    def remove(self, node):
        j = 0
        temp = self.head
        prev = None
        while temp!=node and temp is not None:
            prev = temp
            temp = temp.next
            j += 1
        
        
        if temp:
            if prev is None:
                
                self.head = temp.next
            else:
                prev.next = temp.next

            
            if temp == self.last:
                self.last = prev

            
            if self.present == temp:
                self.present = self.head if self.head else None 
    def get_last(self):
        return self.last
    def Get_length(self):
        self.length=0
        temp=self.head 
        j=0 
        while temp:
            temp=temp.next 
            j+=1 
        return j
        

class Implement(QWidget):
    
    def __init__(self):
        super().__init__()
        self.present=Node()
        self.tab=Tabs()

        self.Window()
    
    def Window(self):
        self.layout=QVBoxLayout() 
        self.btnLayout=QHBoxLayout()
        self.button=QPushButton("New Tab")
        self.button.clicked.connect(self.add_Tab)
        self.button=QPushButton("delete Tab")
        self.button.clicked.connect(self.delete_Tab)
        self.button=QPushButton("Next Tab")
        self.button.clicked.connect(self.next_Tab)
        self.button=QPushButton("prev Tab")
        self.button.clicked.connect(self.prev_Tab)

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.present.data)
        self.setLayout(self.layout)
        
        
    def add_Tab(self):
        k=Node()
        self.tab.add(k) 
        self.layout.removeWidget(self.present.data)
        self.layout.addWidget(k.data)
        self.present=k 
    
        

        





if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Implement()
    window.showMaximized()
    sys.exit(app.exec())

