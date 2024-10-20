
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
            t=self.last
            self.last.next=node 
            node.prev=self.last
            self.last=node 
             
    def remove(self, node):
       
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
        
        elif node == self.last:
            self.last = node.prev
            if self.last:
                self.last.next = None
       
        else:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

       
        if self.present == node:
            self.present = self.head if self.head else None
    def get_last(self):
        return self.last
    def Get_length(self):
        self.length=0
        temp=self.last
        j=0 
        while temp:
            temp=temp.prev
            j+=1 
        return j
    def get_prev(self,node):
        if node.prev:
            return node.prev 
            print("sucess")
        else:
            print("noo")
            return node
    def get_next(self,node):
        if node.next:
            return node.next
            print("sucess")
        else:
            return node
         

class Implement(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,800,600)
        self.setStyleSheet("""QPushButton {
        background-color: #4CAF50; 
        color: white; 
        border: 2px green solid; 
        padding: 5px; 
        border-radius: 5px; 
        font-size: 10px; 
    }
    """)
        self.present=Node()
        self.tab=Tabs()
        self.tab.add(self.present)
        self.Window()
    
    def Window(self):
        self.layout=QVBoxLayout() 
        self.btnLayout=QHBoxLayout()
        self.buttonnew=QPushButton("New Tab")
        self.buttonnew.clicked.connect(self.add_Tab)
        self.buttondel=QPushButton("delete Tab")
        self.buttondel.clicked.connect(self.delete_Tab)
        self.buttonnext=QPushButton("Next Tab")
        self.buttonnext.clicked.connect(self.next_Tab)
        self.buttonprev=QPushButton("prev Tab")
        self.buttonprev.clicked.connect(self.prev_Tab)
        self.btnLayout.addWidget(self.buttonprev)
        self.btnLayout.addWidget(self.buttonnew)
        self.btnLayout.addWidget(self.buttonnext)
        self.btnLayout.addWidget(self.buttondel)
        self.layout.addLayout(self.btnLayout)
        self.layout.addWidget(self.present.data)
        self.setLayout(self.layout)
        
        
    def add_Tab(self):
        k=Node()
        self.tab.add(k)
        print(k.data)
        self.layout.removeWidget(self.present.data)
        self.layout.addWidget(k.data)
        self.present=k 
    def prev_Tab(self):
        k=self.tab.get_prev(self.present)
        print(k.data)
        self.layout.removeWidget(self.present.data)
        self.present.data.setParent(None)
        self.layout.addWidget(k.data)
        self.present=k
        print("prevlenght")
        print(self.tab.Get_length())
    def next_Tab(self):
        k=self.tab.get_next(self.present)
        self.layout.removeWidget(self.present.data)
        self.present.data.setParent(None)
        self.layout.addWidget(k.data)
        self.present=k
        
        print("nextlenght")
        print(self.tab.Get_length())
    def delete_Tab(self):
        m=self.present 
        self.tab.remove(m)
        k=self.tab.get_next(self.present)
        self.layout.removeWidget(self.present.data)
        self.present.data.setParent(None)
        self.layout.addWidget(k.data)
        self.present=k
        print("dellenght")
        print(self.tab.Get_length())

        

    
        

        





if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Implement()
    window.show()
    sys.exit(app.exec())

