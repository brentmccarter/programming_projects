import requests
import time
import tkinter as tk


class WeatherGUI():
    def __init__(self,tkinter_object : tk):
        self.canvas = tkinter_object
        self.canvas.geometry("600x500")
        self.canvas.title("Weather App")
        
        self.gui_font = ("poppins",35, "bold")

        self.user_input = ""
        self.textfield = tk.Entry(self.canvas,font = self.gui_font)
        self.textfield.pack(pady=20)
        self.textfield.focus()


        self.label1 = tk.Label(self.canvas, font= self.gui_font)
        self.label1.pack()
        self.label2=tk.Label(self.canvas,font = self.gui_font)
        

    def run(self):
        self.canvas.mainloop()



class WeatherAPI():
    def __init__(self):
        pass

    def get_weather(self):
        pass

tk_object = tk.Tk()
weather_gui =WeatherGUI(tk_object)
weather_gui.run()
