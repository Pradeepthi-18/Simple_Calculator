import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("300x400")
        self.configure(bg="#f0f0f0")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.create_widgets()

    def create_widgets(self):
        result_entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=4, width=15, justify='right', bg="#d3d3d3")
        result_entry.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")

        buttons = [
            ('AC', 1, 0), ('%', 1, 1), ('CE', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('00', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
        ]

        for (text, row, col) in buttons:
            button_color = "#262626" if text not in ['AC', '='] else "#0000FF" if text == 'AC' else "#FFA500"
            text_color = "#FFFFFF" if text != 'AC' else "#FFFFFF"
            button = tk.Button(self, text=text, font=('Arial', 18), width=5, height=1, padx=20, pady=20, bg=button_color, fg=text_color, bd=5, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)

    def on_button_click(self, value):
        current_text = self.result_var.get()

        if value == 'AC':
            self.result_var.set('')
        elif value == '=':
            try:
                result = str(eval(current_text))
                self.result_var.set(result)
            except:
                self.result_var.set('Error')
        elif value == 'CE':
            self.result_var.set(current_text[:-1])
        else:
            if current_text == 'Error':
                self.result_var.set(value)
            else:
                self.result_var.set(current_text + value)


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
