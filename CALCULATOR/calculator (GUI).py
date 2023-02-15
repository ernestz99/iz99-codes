from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        # Create a label widget to display the calculator result
        self.display = Label(master, text="0", width=28, height=2, bg="white", anchor="e")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Create the calculator buttons
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("+", 4, 3)
        self.create_button("=", 5, 0, columnspan=4)
        
        self.equation = ""
        self.total = 0
        
    def create_button(self, text, row, column, rowspan=1, columnspan=1):
        button = Button(self.master, text=text, width=6, height=2, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=5, pady=5)
        
    def button_click(self, text):
        if text == "C":
            self.equation = ""
            self.total = 0
            self.display.config(text="0")
        elif text == "=":
            self.total = eval(self.equation)
            self.display.config(text=str(self.total))
        else:
            self.equation += text
            self.display.config(text=self.equation)

# Create the Tkinter window
root = Tk()

# Create the calculator instance
calculator = Calculator(root)

# Start the Tkinter event loop
root.mainloop()
