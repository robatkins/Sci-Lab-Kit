import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculate_power():
    try:
        volts = float(entry_volts.get())
        amps = float(entry_amps.get())

        watts = volts * amps
        label_result.config(text=f"Power (Watts): {watts:.2f}")

        # Store current values for future use
        calculate_power.current_values = volts, amps
    except ValueError:
        label_result.config(text="Invalid input. Please enter numeric values for Volts and Amps.")

def calculate_current():
    try:
        volts = float(entry_volts.get())
        resistance = float(entry_resistance.get())

        current = volts / resistance
        label_result.config(text=f"Current (Amps): {current:.2f}")

        # Store current values for future use
        calculate_current.current_values = volts, resistance
    except ValueError:
        label_result.config(text="Invalid input. Please enter numeric values for Volts and Resistance.")

def display_calculation():
    try:
        time_interval = int(entry_time_interval.get())
        if time_interval <= 0:
            raise ValueError("Time interval must be greater than zero.")

        volts, amps = calculate_power.current_values
        resistance = calculate_current.current_values[1]

        if var_graph_type.get() == 0:  # Power
            power = volts * amps
            total_power = power * time_interval
            label_result.config(text=f"Total Power (Watt-seconds): {total_power:.2f}")
        else:  # Resistance
            total_resistance = resistance * time_interval
            label_result.config(text=f"Total Resistance (Ohm-seconds): {total_resistance:.2f}")

    except ValueError as e:
        label_result.config(text=str(e))
    except Exception as e:
        label_result.config(text="An error occurred during calculation.")


# Create main window
root = tk.Tk()
root.title("Electrician Tool")

# Create and place widgets using pack for centering
label_volts = ttk.Label(root, text="Volts:")
label_volts.pack(padx=10, pady=10, side=tk.LEFT)

entry_volts = ttk.Entry(root)
entry_volts.pack(padx=10, pady=10, side=tk.LEFT)

label_amps = ttk.Label(root, text="Amps:")
label_amps.pack(padx=10, pady=10, side=tk.LEFT)

entry_amps = ttk.Entry(root)
entry_amps.pack(padx=10, pady=10, side=tk.LEFT)

button_calculate_power = ttk.Button(root, text="Calculate Power", command=calculate_power)
button_calculate_power.pack(padx=10, pady=10, side=tk.LEFT)

label_resistance = ttk.Label(root, text="Resistance (Ohms):")
label_resistance.pack(padx=10, pady=10, side=tk.LEFT)

entry_resistance = ttk.Entry(root)
entry_resistance.pack(padx=10, pady=10, side=tk.LEFT)

button_calculate_current = ttk.Button(root, text="Calculate Current", command=calculate_current)
button_calculate_current.pack(padx=10, pady=10, side=tk.LEFT)

label_result = ttk.Label(root, text="")
label_result.pack(padx=10, pady=10, side=tk.LEFT)

label_time_interval = ttk.Label(root, text="Time Interval (seconds):")
label_time_interval.pack(padx=10, pady=10, side=tk.LEFT)

entry_time_interval = ttk.Entry(root)
entry_time_interval.pack(padx=10, pady=10, side=tk.LEFT)

var_graph_type = tk.IntVar(value=0)  # 0 for Power, 1 for Resistance

radio_power = ttk.Radiobutton(root, text="Power", variable=var_graph_type, value=0)
radio_power.pack(padx=10, pady=10, side=tk.LEFT)

radio_resistance = ttk.Radiobutton(root, text="Resistance", variable=var_graph_type, value=1)
radio_resistance.pack(padx=10, pady=10, side=tk.LEFT)

button_display_calculation = ttk.Button(root, text="Display Calculation", command=display_calculation)
button_display_calculation.pack(padx=10, pady=10, side=tk.LEFT)


# Run the main loop
root.mainloop()
