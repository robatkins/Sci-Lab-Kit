#Potential Energy Calculator

def calculate_potential_energy(mass, height):
    # Acceleration due to gravity on Earth (m/s^2)
    gravity = 9.8
    
    # Calculate potential energy using the formula PE = m * g * h
    potential_energy = mass * gravity * height
    
    return potential_energy

def main():
    try:
        # Get user input for mass and height
        mass = float(input("Enter the mass of the object (in kilograms): "))
        height = float(input("Enter the height above the reference point (in meters): "))
        
        # Calculate potential energy
        energy = calculate_potential_energy(mass, height)
        
        # Display the result
        print(f"The potential energy of the object is {energy:.2f} joules.")
    
    except ValueError:
        print("Invalid input. Please enter valid numerical values for mass and height.")

if __name__ == "__main__":
    main()
