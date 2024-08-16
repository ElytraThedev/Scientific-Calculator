from tkinter import *
class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("330x325")
        self.root.config(bg="#333333")
        self.root.resizable(False, False)
        self.resultwindow = Entry(self.root, font=("Helvetica", 18), borderwidth=4, relief=SUNKEN, bg="#ffffff")
        self.resultwindow.grid(row=0, column=0, columnspan=6, pady=10)
        self.resultwindow.focus_set()
        buttons = [('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3), ('-', 1, 4),('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('/', 2, 4),('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('C', 3, 4), ('Del', 3, 3),('0', 4, 0), ('(', 4, 1), (')', 4, 2), ('=', 4, 3, 2)]
        for text, row, col, *span in buttons:
            span = span[0] if span else 1
            Button(self.root, text=text, width=5, height=2, font=("Helvetica", 14),
                   command=lambda t=text: self.handle_button(t), relief=RAISED,
                   bg=self.get_button_color(text), fg='black').grid(row=row, column=col, columnspan=span, padx=2, pady=2)
    def get_button_color(self, text):
        colors = {'C': '#FF6347','Del': '#FF4500','=': '#32CD32',}
        return colors.get(text, '#87CEEB')  # SkyBlue for default
    def handle_button(self, text):
        if text == "=":
            self.calculate()
        elif text == "C":
            self.resultwindow.delete(0, 'end')
        elif text == "Del":
            current_text = self.resultwindow.get()
            self.resultwindow.delete(0, 'end')
            self.resultwindow.insert(0, current_text[:-1])
        else:
            self.resultwindow.insert(END, text)
    def calculate(self):
        try:
            result = eval(self.resultwindow.get(), {"__builtins__": None}, {})
            self.resultwindow.delete(0, 'end')
            self.resultwindow.insert(0, result)
        except Exception:
            self.resultwindow.delete(0, 'end')
            self.resultwindow.insert(0, "Error")
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    Calculator().run()