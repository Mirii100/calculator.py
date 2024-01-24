import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("400x400")  # Adjusted window size for better visibility

text_result = tk.Text(root, height=2, width=16, font=("arial", 24))
text_result.grid(row=0, column=0, columnspan=5, pady=10)  # Added pady for padding

buttons = [
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    "0", "(", ")", "/"
]

row_val = 1
col_val = 0

for button_text in buttons:
    btn = tk.Button(root, text=button_text, width=5, font=("Arial", 14),
                    command=lambda text=button_text: add_to_calculation(text))
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)  # Added padx and pady for margin
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=5, font=("Arial", 14))
btn_equals.grid(row=row_val, column=col_val, columnspan=2, padx=5, pady=5)  # Added padx and pady for margin

btn_clear = tk.Button(root, text="C", command=clear_field, width=10, font=("Arial", 14))
btn_clear.grid(row=row_val + 1, column=0, columnspan=4, padx=5, pady=10)  # Added padx and pady for margin

root.mainloop()
