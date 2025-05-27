import tkinter as tk

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget to display input/output
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Button layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
]

# Create and place buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for char in row:
        if char == "=":
            btn = tk.Button(frame, text=char, font=("Arial", 18), command=calculate)
        else:
            btn = tk.Button(frame, text=char, font=("Arial", 18),
                            command=lambda ch=char: press(ch))
        btn.pack(side="left", expand=True, fill="both")

# Clear button
clear_btn = tk.Button(root, text="Clear", font=("Arial", 18), bg="red", fg="white", command=clear)
clear_btn.pack(side="bottom", fill="both")

# Run the application
root.mainloop()
