from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    
    def __init__(self):
        Tk.__init__(self)
                
        self.geometry("210x150")
        self.title("Termómetro")
        self.configure(bg = "#ECECEC")
        self.resizable(0,0)
        
        self.temperatura = StringVar(value="")
        self.tipoUnidad = StringVar(value="C")
        
        self.createLayout()
        
    def createLayout(self):
        self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=10, y=10)
        
        self.lbUnidad = ttk.Label(self, text="Grados:").place(x=10, y=45)
        self.rb1 = ttk.Radiobutton(self, text="Farenheit", variable=self.tipoUnidad, value="F").place(x=20, y=70)
        self.rb2 = ttk.Radiobutton(self, text="Celsius", variable=self.tipoUnidad, value="C").place(x=20, y=95)
    
    def start(self):
        self.mainloop()
        
        
if __name__ == '__main__':
    app = mainApp()
    app.start()
    
