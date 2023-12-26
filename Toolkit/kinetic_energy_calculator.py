#Kinetic Energy Calculator

def calculate_kinetic_energy(mass, velocity):
    # Calculate kinetic energy using the formula KE = 0.5 * m * v^2
    kinetic_energy = 0.5 * mass * velocity**2
    
    return kinetic_energy

def main():
    try:
        # Get user input for mass and velocity
        mass = float(input("Enter the mass of the object (in kilograms): "))
        velocity = float(input("Enter the velocity of the object (in meters per second): "))
        
        # Calculate kinetic energy
        energy = calculate_kinetic_energy(mass, velocity)
        
        # Display the result
        print(f"The kinetic energy of the object is {energy:.2f} joules.")
    
    except ValueError:
        print("Invalid input. Please enter valid numerical values for mass and velocity.")

if __name__ == "__main__":
    main()
