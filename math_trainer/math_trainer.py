from tkinter import *
import random


class Game():
    def __init__(self,number_of_questions = -1,timer_mode = False, debug = False):
        self.debug = debug
        self.window = Tk()
        self.window.title("Math Game")
        self.window.resizable(False,False)
        self.window.geometry("500x500")
        self.window.attributes(topmost=True)
        
        self.input_numbers = ""
        self.correct_answer = 0
        self.correct = 0 
        self.incorrect = 0

        self.top_frame = Frame(self.window, background = "#00FF00")
        self.toplabel = Label(self.top_frame, text = ("Ready?"))

        self.results = Label(self.top_frame, text = "0")

        
        self.math_frame = Frame(self.window, bg = "blue",)
        self.math_frame.columnconfigure(0,weight = 1)
        self.math_frame.columnconfigure(1,weight = 1)
        self.math_frame.columnconfigure(2,weight = 1)
        self.math_frame.columnconfigure(3,weight = 1)
        self.math_frame.columnconfigure(4,weight = 1)
        
        self.math_frame.rowconfigure(0,weight = 1)
        self.math_frame.rowconfigure(1,weight = 1)
        self.math_frame.rowconfigure(2,weight = 1)
        self.math_frame.rowconfigure(3,weight = 1)

        self.top_frame.pack(expand = True, fill = "both")
        self.toplabel.pack(expand = True, fill= "both")

        self.math_frame.pack(expand = True, fill = "both")


    def button_press(self,input):
        match input:
            case "0":
                    if  self.input_numbers != "" and self.input_numbers !="0" and self.input_numbers!="Cleared":
                        self.input_numbers += "0"
                        self.input_label.config(text = self.input_numbers)

            case "1":
                self.input_numbers += "1"
                self.input_label.config(text = self.input_numbers)
            case "2":
                self.input_numbers += "2"
                self.input_label.config(text = self.input_numbers)
            case "3":
                self.input_numbers += "3"
                self.input_label.config(text = self.input_numbers)
            case "4":
                self.input_numbers += "4"
                self.input_label.config(text = self.input_numbers)
            case "5":
                self.input_numbers += "5"
                self.input_label.config(text = self.input_numbers)
            case "6":
                self.input_numbers += "6"
                self.input_label.config(text = self.input_numbers)
            case "7":
                self.input_numbers += "7"
                self.input_label.config(text = self.input_numbers)
            case "8":
                self.input_numbers += "8"
                self.input_label.config(text = self.input_numbers)
            case "9":
                self.input_numbers += "9"
                self.input_label.config(text = self.input_numbers)
            case "e":
                self.input_label.config(text = "Entered")
                if int(self.input_numbers) == self.correct_answer:
                    self.correct+=1
                    self.toplabel.config(text="Correct!")
                    left,right,answer,operation = self.new_number()
                    self.correct_answer=answer
                    self.toplabel.config(text = f"{left}{operation}{right}")

                else:
                    self.incorrect +=1
                    self.toplabel.config(text="Incorrect.")
                    left,right,answer,operation = self.new_number()
                    self.correct_answer=answer
                    self.toplabel.config(text = f"{left}{operation}{right}")
                self.input_numbers=""
                self.results.config(text=f"Correct: {self.correct} Incorrect: {self.incorrect}")
            case "d":
                self.input_label.config(text = "Cleared")
                self.input_numbers = ""
            


    def math_game(self, timer_mode = False):
        self.input_label = Label(self.top_frame, text = "Input a number to start.")

        self.button0 = Button(self.math_frame, text = "0",command = lambda: self.button_press("0"))
        self.button1 = Button(self.math_frame, text = "1", command = lambda: self.button_press("1"))
        self.button2 = Button(self.math_frame, text = "2", command = lambda: self.button_press("2"))
        self.button3 = Button(self.math_frame, text = "3", command = lambda: self.button_press("3"))
        self.button4 = Button(self.math_frame, text = "4", command = lambda: self.button_press("4"))
        self.button5 = Button(self.math_frame, text = "5", command = lambda: self.button_press("5"))
        self.button6 = Button(self.math_frame, text = "6", command = lambda: self.button_press("6"))
        self.button7 = Button(self.math_frame, text = "7", command = lambda: self.button_press("7"))
        self.button8 = Button(self.math_frame, text = "8", command = lambda: self.button_press("8"))
        self.button9 = Button(self.math_frame, text = "9", command = lambda: self.button_press("9"))
        self.button_e = Button(self.math_frame, text = "Enter", command = lambda: self.button_press("e"))
        self.button_d = Button(self.math_frame, text = "Clear", command = lambda: self.button_press("d"))
        
        self.input_label.pack(expand = True, fill = "both")
        self.results.pack(expand = True, fill = "both")
        self.button0.grid(column = 0,row = 0,sticky = "news")
        self.button1.grid(column = 1,row = 0,sticky = "news")
        self.button2.grid(column = 2,row = 0,sticky = "news" )
        self.button3.grid(column = 3,row = 0, sticky = "news")
        self.button4.grid(column = 0,row = 1,sticky = "news" )
        self.button5.grid(column = 1,row = 1,sticky = "news" )
        self.button6.grid(column = 2,row = 1,sticky = "news" )
        self.button7.grid(column = 3,row = 1, sticky = "news")
        self.button8.grid(column = 0,row = 2,sticky = "news")
        self.button9.grid(column = 1,row = 2,sticky = "news")
        self.button_e.grid(column = 4, row = 0,sticky = "news")
        self.button_d.grid(column = 4, row = 1,sticky = "news")


        left,right,answer,operation = self.new_number()
        self.toplabel.config(text = f"{left}{operation}{right}")
        self.window.mainloop()

    def new_number(self,mode = "addition"):
        left = random.randint(1,50)
        right = random.randint(1,50)

        if mode =="addition":
            answer = left + right
            operation = "+"

        return  left,right, answer, operation


g = Game(debug = True)
g.math_game()
