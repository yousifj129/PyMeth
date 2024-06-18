
import matplotlib.pyplot as plt 
import numpy as np 
import time
from threading import Thread
class animationSettings():
    def __init__(self,width = 1280, height = 720, speed = 0.5, start = 0, end = 100, num = 100):
        self.width = width
        self.height = height
        self.speed = speed
        self.start = start
        self.end = end
        self.num = num
        

class methanimator():
    def __init__(self, func:callable, settings:animationSettings):
        plt.ion() 
        self.fig = plt.figure()
        self.fig.set_figwidth(settings.width/self.fig.dpi)
        self.fig.set_figheight(settings.height/self.fig.dpi)
        x = np.linspace(settings.start, settings.end, settings.num) 
        y = func(x)
        self.ax = self.fig.add_subplot(111)
        line1, = self.ax.plot(x, y, 'b-') 
  
        for phase in np.linspace(settings.start, settings.end, settings.num): 
            line1.set_ydata(func(0.5* x + phase*settings.speed)) 
            self.fig.canvas.draw() 
            self.fig.canvas.flush_events() 
            
