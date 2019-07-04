import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        
        self.setGeometry(70, 30, 1230, 670)
        self.setWindowTitle('FPS in piece')
        self.show()
        

    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        self.draw_What_Ever_You_Want(qp)
        qp.end()
        
        
    def draw_What_Ever_You_Want(self, qp):

    	# qp.setPen()
    	qp.setBrush(Qt.green)
    	qp.drawRect(500,200,1,1)
                
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
