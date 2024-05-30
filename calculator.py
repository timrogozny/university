import tkinter as tk
from gradient_generator import generate_gradient



bigfont = ("Arial", 40, "bold")
digitfont = ("Arial", 24, "bold")
smallfont = ("Arial", 20)
calcfont = ("Arial", 30)

darkgreen = "#3B6558"
lightgreen ="#619383"
pink = "#FF5F6C"
yellow = "#F9C241"



class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x650")
        self.window.resizable(0,0)
        self.window.title("Pretty Calc :)")
        self.window.iconbitmap(r'C:/Users/admin/Desktop/файлы игра/set.png')

        self.total = ""
        self.current = ""
        self.frame = self.create_frame()
        self.total_label, self.label = self.create_labels()

        self.digits = {
            7:(1,1), 8:(1,2),9:(1, 3),
            4:(2, 1), 5:(2, 2),6:(2, 3),
            1: (3, 1), 2: (3, 2), 3:(3, 3),
            0:(4,2), ".":(4,1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.bframe = self.create_bframes()


        self.bframe.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.bframe.rowconfigure(x, weight= 1)
            self.bframe.columnconfigure(x, weight=1)
        self.createbuttons()
        self.create_operator()
        self.create_specials()


    def create_specials(self):
        self.createclear()
        self.createquals()
        self.createconverter()
        self.createdegree()




    def create_labels(self):
        total_label = tk.Label(self.frame, text = self.total, anchor = tk.E, bg = lightgreen,
                               fg = yellow, padx = 24,font=smallfont)
        total_label.pack(expand=True, fill = "both")

        label = tk.Label(self.frame, text=self.current, anchor=tk.E, bg=lightgreen,
                               fg=pink, padx=24, font=bigfont)
        label.pack(expand=True, fill="both")
        return total_label,label


    def create_frame(self):
        frame = tk.Frame(self.window, height=10, bg = darkgreen)
        frame.pack(expand=True, fill = "both")
        return frame

    def add_to_expression(self, value):
        self.current += str(value)
        self.update_label()
    def createbuttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.bframe, text = str(digit), bg = darkgreen, fg = yellow, font = digitfont,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression((x)))
            button.grid(row=grid_value[0], column = grid_value[1],sticky = tk.NSEW)

    def append_operator(self, operator):
        self.current += operator
        self.total += self.current
        self.current += ""
        self.update_total_label()
        self.update_label()

    def create_operator(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.bframe, text=symbol, bg=pink, fg =lightgreen, font = calcfont,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row = i, column = 4, sticky =tk.NSEW)
            i += 1

    def clear(self):
        self.current =""
        self.total = ""
        self.update_total_label()
        self.update_label()
    def createclear(self):
        button = tk.Button(self.bframe, text="C", bg=pink, fg=lightgreen, font=calcfont,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, columnspan =1, sticky=tk.NSEW)


    def createconverter(self):
        button = tk.Button(self.bframe, text="$", bg=pink, fg=lightgreen, font=calcfont,
                           borderwidth=0)
        button.grid(row=0, column=2, columnspan =1, sticky=tk.NSEW)


    def createdegree(self):
        button = tk.Button(self.bframe, text="^", bg=pink, fg=lightgreen, font=calcfont,
                           borderwidth=0)
        button.grid(row=0, column=3, columnspan=1, sticky=tk.NSEW)

    def evaluate(self):
        self.total += self.current
        self.update_total_label()

        self.current = str(eval(self.total))
        self.update_label()
        self.total = ""

    def createquals(self):
        button = tk.Button(self.bframe, text="=", bg=pink, fg=pink, font=calcfont,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan =2, sticky=tk.NSEW)


    def create_bframes(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill = "both")
        return frame





    def update_total_label(self):
        self.total_label.config(text = self.total)

    def update_label(self):
        self.label.config(text=self.current)
    def run(self):
        self.window.mainloop()

calc = Calculator()
calc.run()
