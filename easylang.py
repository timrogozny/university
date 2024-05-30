import tkinter as tk
import random


bigfont = ("Code Pro", 60, "bold")
digitfont = ("Arial", 24, "bold")
smallfont = ("Arial", 20, "bold")
mediumfont = ("Arial", 25, "bold")
rogoznyfont = ("Luminari", 15, "bold")
pastel_dark_green = "#5D5D3E"
pastel_ochre = "#B09E6A"
pastel_dark_blue = "#495867"
pastel_pink = "#BFA2DB"
pastel_light_green = "#96BB7C"
pastel_red = "#CC7F5D"
white = "#FFFFFF"




class Langapp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x650")
        self.window.resizable(0, 0)
        self.window.title("easy language app")
        self.window.config(bg=pastel_dark_green)
        self.window.iconbitmap("easylangicon.png")
        self.entry = None

        self.words = {
            "apple": "яблоко",
            "home": "дом",
            "suit": "костюм",
            "noise": "шум",
            "day": "день",
        }

        self.current_word = None
        self.correct_count = 0
        self.incorrect_count = 0

        self.create_widgets()
        self.run()

    def create_widgets(self):
        self.label = tk.Label(self.window, text="EASYLANG", fg=pastel_pink, bg=pastel_dark_green, font=bigfont)
        self.label.pack(pady=10)

        self.start_button = tk.Button(self.window, text="Study!", command=self.start_study,
                                      fg=pastel_dark_blue, bg=pastel_ochre, font=bigfont, relief=tk.RAISED, bd=2)
        self.start_button.pack(pady=140)

        self.result_label = tk.Label(self.window, text="", fg=pastel_dark_blue, bg=pastel_dark_green, font=smallfont)
        self.result_label.pack(pady=10)

        self.correct_label = tk.Label(self.window, text="Correct: 0", fg=pastel_light_green, bg=pastel_dark_green,
                                      font=smallfont)
        self.correct_label.pack(side=tk.LEFT, padx=20, pady=5)

        self.incorrect_label = tk.Label(self.window, text="Incorrect: 0", fg=pastel_red, bg=pastel_dark_green,
                                        font=smallfont)
        self.incorrect_label.pack(side=tk.RIGHT, padx=20, pady=5)

        self.exit = tk.Button(self.window, text="X", fg="red", bg=white, font=mediumfont, command=self.window.destroy,
                              relief=tk.RAISED, bd=2)
        self.exit.place(relx=1.0, rely=1.0, anchor=tk.SE, x=-10, y=-10)

        self.rogoz = tk.Label(self.window, text="by Rogozny", font=rogoznyfont, bg=pastel_dark_green, fg="black")
        self.rogoz.place(relx=1.0, rely=1.0, anchor=tk.SE, x=-300, y=-20)
        self.icon = tk

        #self.image = tk.PhotoImage(file="easylangicon.png")
        #self.image_label = tk.Label(self.window, image=self.image, bg=pastel_dark_green)
        #self.image_label.place(x=10, y=10)


    def start_study(self):
        self.new_word()

        # Hide the start button
        self.start_button.pack_forget()

        # Create and pack the entry field
        self.entry = tk.Entry(self.window, font=mediumfont, bg=pastel_dark_green)
        self.entry.pack(pady=10)

        # Create and pack the submit button
        self.submit_button = tk.Button(self.window,bg=pastel_dark_green, text="Submit", command=self.check_translation, fg=pastel_dark_blue,
                                        font=mediumfont, relief=tk.RAISED, bd=2)
        self.submit_button.pack(pady=10)

        # Create and pack the clear button
        self.clear_button = tk.Button(self.window, text="Clear", command=self.clear_entry, fg="red", bg=pastel_red,
                                      font=smallfont, relief=tk.RAISED, bd=2)
        self.clear_button.pack(pady=10)

    def new_word(self):
        self.clear_entry()
        self.current_word = random.choice(list(self.words.keys()))
        self.label.configure(text=self.current_word)
        self.result_label.configure(text="")

    def clear_entry(self):
        if self.entry:
            self.entry.delete(0, tk.END)

    def check_translation(self):
        translation = self.entry.get().strip().lower()
        if translation == self.words.get(self.current_word, "").lower():
            self.correct_count += 1
            self.correct_label.configure(text=f"Correct: {self.correct_count}")
            self.result_label.configure(text="Correct translation!", fg=pastel_light_green)
            self.window.after(2000, self.new_word)
        else:
            self.incorrect_count += 1
            self.incorrect_label.configure(text=f"Incorrect: {self.incorrect_count}")
            self.result_label.configure(text="Incorrect translation. Try again.", fg=pastel_red)
            self.clear_entry()

    def run(self):
        self.window.mainloop()
    def __exit__(self):
        self.window.destroy



language = Langapp()
language.run()
