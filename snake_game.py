from tkinter import *
from PIL import Image,ImageTk

class Snake(Canvas):
    def __init__(self):
        super().__init__(width=600,height=620,background='black',higlightthickness=0)
        
        self.snake_positions = [(100,100),(80,100),(60,100)]


    def load_assets(self):
        self.snake_body_immage = Image.open('')


GUI = Tk()
GUI.title('Snake Game Nokia 3310')
GUI.resizable(False,False)

GUI.mainloop()

