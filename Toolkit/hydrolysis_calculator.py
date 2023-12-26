#Hydrolysis Calculator
def calculate_hydrolysis(voltage, time):
    # Constants
    faraday_constant = 96485.3329  # Faraday's constant in C/mol
    molar_ratio_h2o = 2  # Hydrogen to Oxygen molar ratio

    # Calculate current using Ohm's Law: V = IR => I = V/R
    resistance = 1.0  # Assuming a resistance of 1 Ohm for simplicity
    current = voltage / resistance

    # Calculate charge (Coulombs) using Q = It
    charge = current * time

    # Calculate moles of water electrolyzed
    moles_water = charge / faraday_constant

    # Calculate moles of hydrogen and oxygen produced
    moles_hydrogen = moles_water / (1 + molar_ratio_h2o)
    moles_oxygen = molar_ratio_h2o * moles_hydrogen

    return moles_hydrogen, moles_oxygen

# Get user input
voltage = float(input("Enter voltage (V): "))
time = float(input("Enter time (s): "))

# Calculate and display results
hydrogen, oxygen = calculate_hydrolysis(voltage, time)
print(f"Amount of Hydrogen produced: {hydrogen} moles")
print(f"Amount of Oxygen produced: {oxygen} moles")
