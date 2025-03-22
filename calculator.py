from tkinter import *

# Function to update input field
def button_click(number):
    current = entry_var.get()
    entry_var.set(current + str(number))

# Function to clear input field
def button_clear():
    entry_var.set("")

# Function to evaluate the expression
def button_equal():
    try:
        result = str(eval(entry_var.get()))  # Evaluate the mathematical expression
        entry_var.set(result)
    except:
        entry_var.set("Error")  # Handle invalid inputs

# Create main window
root = Tk()
root.title("Basic Calculator")
root.geometry("300x400")

# Entry field
entry_var = StringVar()
entry = Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10, relief=RIDGE)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Button Layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Adding buttons dynamically
for text, row, col in buttons:
    if text == "=":
        Button(root, text=text, font=("Arial", 14), command=button_equal, height=2, width=5).grid(row=row, column=col, padx=5, pady=5)
    elif text == "C":
        Button(root, text=text, font=("Arial", 14), command=button_clear, height=2, width=5, bg="red", fg="white").grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=text, font=("Arial", 14), command=lambda t=text: button_click(t), height=2, width=5).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
