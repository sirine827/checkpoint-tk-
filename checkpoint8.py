import tkinter as tk

def fahrenheit_to_celsius():
    """Convert Fahrenheit to Celsius and update the result label."""
    try:
        fahrenheit = float(ent_temperature.get())
        celsius = (fahrenheit - 32) * 5 / 9
        lbl_result.config(text=f"{round(celsius, 2)} \N{DEGREE CELSIUS}")
    except ValueError:
        lbl_result.config(text="Invalid input")

# Create main window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Create entry frame
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Arrange entry widgets
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Create conversion button
btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)

# Create result label
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Arrange widgets
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()

