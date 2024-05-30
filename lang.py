import tkinter as tk
import random


class Langapp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language App")

        self.words = {
            "dog": "собака",
            "cat": "кот",
            "bird": "птица",
            "horse": "лошадь",
            "rabbit": "кролик"
        }

        self.label = tk.Label(self.root, text="Enter the word in Russian:")
        self.label.pack()

        self.random_word = random.choice(list(self.words.keys()))
        self.label_word = tk.Label(self.root, text=self.random_word, font=("Arial", 14))
        self.label_word.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.check_button = tk.Button(self.root, text="Check", command=self.check_translation)
        self.check_button.pack()

    def check_translation(self):
        translation = self.entry.get().strip()
        if translation.lower() == self.words.get(self.random_word):
            result = "Correct translation!"
        else:
            result = "Incorrect translation. Try again."

        self.label.config(text=result)
        self.random_word = random.choice(list(self.words.keys()))
        self.label_word.config(text=self.random_word)
        self.entry.delete(0, 'end')  # очистить поле ввода


root = tk.Tk()
app = Langapp(root)
root.mainloop()