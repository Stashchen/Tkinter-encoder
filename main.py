import string
from tkinter import *
from tkinter import font
from math import gcd


def encode(frm, key, mod, to, error_msg):
    to.delete("1.0", END)
    letters = string.ascii_uppercase
    result = ''
    for let in frm.get():

        for index, tmp_let in enumerate(letters):
            if let == tmp_let:
                new_index = (index * int(key.get())) % int(mod.get())
                result += letters[new_index]

    to.insert("1.0", result)

    if ((int(mod.get()) / int(key.get())) % 2 == 0) or ((int(key.get()) % 2 == 0) and (int(mod.get()) % 2 == 0)):
        popup(error_msg, mod, key)


def popup(msg, mod, key):
    popup = Tk()
    popup.wm_title("Error")
    error = Label(popup, text="ERROR", font=50)
    error.pack(side="top", fill="x")
    text = Label(popup, text=msg + str(int(int(mod.get()) / gcd(int(mod.get()), int(key.get())))), font=50)
    text.pack()
    B1 = Button(popup, text="Back", command=popup.destroy)
    B1.pack(padx=10, pady=10)
    popup.mainloop()


def decode(frm, key, mod, to, error_msg):
    to.delete("1.0", END)
    letters = string.ascii_uppercase
    result = ''
    for let in frm.get():
        x = 0
        index = letters.find(let)
        while True:
            final_index = (x * int(mod.get()) + index) / int(key.get())
            if int(final_index) == final_index:
                result += letters[int(final_index)]
                break
            else:
                x += 1
    to.insert("1.0", result)

    if int(mod.get()) % 2 == 0 and int(key.get()) % 2 == 0:
        popup(error_msg, mod, key)


class Form:
    def __init__(self, title, col, formula):
        self.title = title
        self.column = col
        self.formula = formula
        self.huge_font = font.Font(size=50)
        self.middle_font = font.Font(size=20)

        self.key = Entry(window, font=self.middle_font)
        self.mod = Entry(window, font=self.middle_font)
        self.data = Entry(window, font=self.middle_font)
        self.result = Text(window, font=self.middle_font, width=50, height=7)
        self.button = Button(window, text="SUBMIT", font=self.middle_font, bg="tan1")

        Label(window, text=self.title, font=self.huge_font, bg="lavender")\
            .grid(row=0, column=self.column, columnspan=2, padx=10, pady=10)
        Label(window, text=self.formula, font=self.middle_font, bg="lavender")\
            .grid(row=1, column=self.column, columnspan=2, padx=10, pady=10)
        Label(window, text="Input data:", font=self.middle_font, bg="lavender")\
            .grid(row=2, column=self.column, padx=5, pady=5)
        Label(window, text="Input key:", font=self.middle_font, bg="lavender") \
            .grid(row=3, column=self.column, padx=5, pady=5)
        Label(window, text="Input mod:", font=self.middle_font, bg="lavender") \
            .grid(row=4, column=self.column, padx=5, pady=5)
        Label(window, text="Result:", font=self.middle_font, bg="lavender") \
            .grid(row=5, column=self.column, columnspan=2, sticky=W, padx=30, pady=5)

        self.data.grid(row=2, column=self.column + 1, sticky=E, padx=30)
        self.key.grid(row=3, column=self.column + 1, sticky=E, padx=30)
        self.mod.grid(row=4, column=self.column + 1, sticky=E, padx=30)
        self.button.grid(row=5, column=self.column, columnspan=2)
        self.result.grid(row=7, column=self.column, columnspan=2, padx=15, pady=15)


if __name__ == '__main__':
    window = Tk()
    window.title("Encoder/Decoder")
    window.config(bg="lavender")

    encoder = Form("Encoder", 0, "I = I*K*mod")
    encoder.button.config(command=lambda: encode(
        encoder.data,
        encoder.key,
        encoder.mod,
        encoder.result,
        "The " + encoder.title + " works wrong. There wrong values will be from letter number: "
    )
    )
    decoder = Form("Decoder", 2, "I = (x*K + i)/mod")
    decoder.button.config(command=lambda: decode(
        decoder.data,
        decoder.key,
        decoder.mod,
        decoder.result,
        "The " + decoder.title + " worked wrong, so there will be wrong values starting from letter number: "
    )
    )
    window.mainloop()
