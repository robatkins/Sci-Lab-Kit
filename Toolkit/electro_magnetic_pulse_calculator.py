#Electromagnetic Pulse Calculator
import math

def calculate_emp_intensity(charge, distance):
    """
    Calculate the EMP intensity based on user input.

    Parameters:
    - charge: Charge of the explosive device (in coulombs).
    - distance: Distance from the explosive device to the point of interest (in meters).

    Returns:
    - emp_intensity: Calculated EMP intensity.
    """
    emp_constant = 8.9875e9  # Coulomb's constant in N m^2 / C^2
    speed_of_light = 3.0e8  # Speed of light in m/s

    emp_intensity = (emp_constant * charge) / (distance * speed_of_light)

    return emp_intensity

def main():
    print("Electromagnetic Pulse (EMP) Calculator")

    # Get user input for charge and distance
    charge = float(input("Enter the charge of the explosive device (in coulombs): "))
    distance = float(input("Enter the distance from the explosive device to the point of interest (in meters): "))

    # Calculate EMP intensity
    emp_intensity = calculate_emp_intensity(charge, distance)

    # Display the result
    print(f"The calculated EMP intensity is {emp_intensity} N/C.")

if __name__ == "__main__":
    main()
