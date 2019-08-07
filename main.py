from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    
    __temperaturaAnt = ""
    
    def __init__(self):
        Tk.__init__(self)
                
        self.geometry("210x150")
        self.title("Termómetro")
        self.configure(bg = "#ECECEC")
        self.resizable(0,0)
        
        self.temperatura = StringVar(value="")
        self.temperatura.trace("w", self.validateTemperature)
        self.tipoUnidad = StringVar(value="C")
        
        self.createLayout()
        
    def createLayout(self):
        self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=10, y=10)
        
        self.lbUnidad = ttk.Label(self, text="Grados:").place(x=10, y=45)
        self.rb1 = ttk.Radiobutton(self, text="Farenheit", variable=self.tipoUnidad, value="F", command=self.selected).place(x=20, y=70)
        self.rb2 = ttk.Radiobutton(self, text="Celsius", variable=self.tipoUnidad, value="C", command=self.selected).place(x=20, y=95)
    
    def start(self):
        self.mainloop()
        
    def validateTemperature(self, *args):
        nuevoValor = self.temperatura.get()
        try:
            float(nuevoValor)
            self.__temperaturaAnt = nuevoValor
        except:
            self.temperatura.set(self.temperaturaAnt)
    
    def selected(self):
        resultado = 0
        toUnidad = self.tipoUnidad.get()
        grados = float(self.temperatura.get())
        
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
        
        self.temperatura.set(resultado)
        
        
if __name__ == '__main__':
    app = mainApp()
    app.start()
    
