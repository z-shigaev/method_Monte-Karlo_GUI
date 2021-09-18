from PyQt5.QtWidgets import QVBoxLayout
import random
from math import sqrt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class Layout(QVBoxLayout):
    def __init__(self, root):
        super().__init__()
        plt.style.use("seaborn-dark")

        self.figure = plt.figure()
        self.ax1 = self.figure.add_subplot()
        # self.ax1.plot(x, y)
        self.canvas = FigureCanvas(self.figure)
        self.addWidget(self.canvas)
    
    def make_plot(self, n):
        self.figure.clear()
        self.ax1 = self.figure.add_subplot()
        circle=0
        x1 = []
        y1 = []
        x2 = []
        y2 = []

        for i in range(0, n):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if sqrt(x*x+y*y) <= 1:
                circle += 1
                x1.append(x)
                y1.append(y)
            else:
                x2.append(x)
                y2.append(y)
        pi = 4*circle/n
        print(pi)
        self.ax1.scatter(x1, y1, c='red', s=1)
        self.ax1.scatter(x2, y2, c='blue', s=1)
        self.canvas.draw()
        return pi
        # plt.show()