import sys

import main_win
import plot_canvas as pc

import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow, main_win.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowIcon(QtGui.QIcon('main_icon.jpg'))
        self.widget_layout = pc.Layout(self.widget)
        self.widget.setLayout(self.widget_layout)
        self.pushButton.clicked.connect(self.plot1)
        
    def plot1(self):
        number = self.spinBox.value()
        if number == 0:
            number = 100
        pi = self.widget_layout.make_plot(number)
        self.lineEdit.setText(str(pi))

def test():
    circle=0
    n=10**6
    x1 = []
    y1 = []
    x2 = []
    y2 = []

    for i in range(0,n):
        x=random.uniform(-1, 1)
        y=random.uniform(-1, 1)
        if sqrt(x*x+y*y)<=1:
            circle+=1
            x1.append(x)
            y1.append(y)
        else:
            x2.append(x)
            y2.append(y)
    pi=4*circle/n
    print (pi)

    fig, ax = plt.subplots()
    fig.set_figwidth(8)    
    fig.set_figheight(8)
    ax.scatter(x1, y1, c = 'red', s = 1)
    ax.scatter(x2, y2, c = 'blue', s = 1)
    plt.show()
    
if __name__ == '__main__':  
    app = QtWidgets.QApplication(sys.argv)  
    window = MainWindow()  
    window.show()  
    app.exec_()  