def calculate_force(mass, acceleration):
    # Newton's second law: F = m * a
    force = mass * acceleration
    return force

def main():
    try:
        # Get user input for mass and acceleration
        mass = float(input("Enter the mass (in kilograms): "))
        acceleration = float(input("Enter the acceleration (in meters per second squared): "))
        
        # Check if mass and acceleration are non-negative
        if mass < 0 or acceleration < 0:
            print("Mass and acceleration must be non-negative.")
        else:
            # Calculate and print the force
            force = calculate_force(mass, acceleration)
            print(f"The force corresponding to a mass of {mass} kg and acceleration of {acceleration} m/s^2 is {force} newtons.")
    except ValueError:
        print("Invalid input. Please enter valid numbers for mass and acceleration.")

if __name__ == "__main__":
    main()
