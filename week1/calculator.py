import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.resizable(False, False)

# Display
entry = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=10
)
entry.pack(fill="both", padx=10, pady=10, ipady=10)

# Buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    
    for btn in row:
        if btn == "=":
            command = calculate
        else:
            command = lambda x=btn: click(x)

        tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 18),
            command=command
        ).pack(side="left", expand=True, fill="both", padx=2, pady=2)

# Clear button
tk.Button(
    root,
    text="Clear",
    font=("Arial", 18),
    command=clear
).pack(fill="both", padx=10, pady=10)

root.mainloop()