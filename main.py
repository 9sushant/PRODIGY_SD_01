import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        temperature = float(temperature_entry.get())
        from_unit = from_unit_var.get()
        
        # Convert to Celsius first
        if from_unit == "Celsius":
            celsius = temperature
        elif from_unit == "Fahrenheit":
            celsius = (temperature - 32) * 5/9
        else:  # Kelvin
            celsius = temperature - 273.15
        
        # Convert Celsius to other units
        fahrenheit = celsius * 9/5 + 32
        kelvin = celsius + 273.15
        
        # Update result labels
        celsius_result.config(text=f"{celsius:.2f} °C")
        fahrenheit_result.config(text=f"{fahrenheit:.2f} °F")
        kelvin_result.config(text=f"{kelvin:.2f} K")
        
    except ValueError:
        celsius_result.config(text="Invalid input")
        fahrenheit_result.config(text="Invalid input")
        kelvin_result.config(text="Invalid input")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")

# Create and place widgets
temperature_label = ttk.Label(root, text="Temperature:")
temperature_label.grid(row=0, column=0, padx=5, pady=5)

temperature_entry = ttk.Entry(root)
temperature_entry.grid(row=0, column=1, padx=5, pady=5)

from_unit_label = ttk.Label(root, text="From Unit:")
from_unit_label.grid(row=1, column=0, padx=5, pady=5)

from_unit_var = tk.StringVar()
from_unit_dropdown = ttk.Combobox(root, textvariable=from_unit_var, values=["Celsius", "Fahrenheit", "Kelvin"])
from_unit_dropdown.grid(row=1, column=1, padx=5, pady=5)
from_unit_dropdown.set("Celsius")

convert_button = ttk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

result_label = ttk.Label(root, text="Results:")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

celsius_result = ttk.Label(root, text="")
celsius_result.grid(row=4, column=0, columnspan=2, padx=5, pady=2)

fahrenheit_result = ttk.Label(root, text="")
fahrenheit_result.grid(row=5, column=0, columnspan=2, padx=5, pady=2)

kelvin_result = ttk.Label(root, text="")
kelvin_result.grid(row=6, column=0, columnspan=2, padx=5, pady=2)

# Start the GUI event loop
root.mainloop()