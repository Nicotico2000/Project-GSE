import tkinter as tk

def on_click(row, col):
    print(f"Button clicked at ({row}, {col})")

root = tk.Tk()
root.title("10x10 Board")

# Create a 10x10 grid of buttons
buttons = []

for i in range(20):
    row_buttons = []
    for j in range(20):
        btn = tk.Button(
            root,
            text=f"{i},{j}",
            width=2,
            height=1,
            command=lambda r=i, c=j: on_click(r, c)
        )
        btn.grid(row=i, column=j)
        row_buttons.append(btn)
    buttons.append(row_buttons)

root.mainloop()