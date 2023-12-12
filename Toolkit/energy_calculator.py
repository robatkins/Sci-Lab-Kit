def pounds_to_kilograms(pounds):
    # Conversion factor from pounds to kilograms
    return pounds * 0.453592

def calculate_energy(mass, is_kilograms=True):
    # Speed of light in meters per second
    speed_of_light = 3e8
    
    # Convert mass to kilograms if it's in pounds
    if not is_kilograms:
        mass = pounds_to_kilograms(mass)
    
    # Energy calculation using E=mc^2
    energy = mass * speed_of_light**2
    
    return energy

def main():
    try:
        # Ask the user for mass input unit
        unit_choice = input("Enter mass unit (pounds or kilograms): ").lower()
        
        if unit_choice not in ['pounds', 'kilograms']:
            print("Invalid unit choice. Please enter 'pounds' or 'kilograms'.")
            return
        
        # Get user input for mass
        mass = float(input(f"Enter the mass (in {unit_choice}): "))
        
        # Check if mass is non-negative
        if mass < 0:
            print("Mass must be non-negative.")
        else:
            # Calculate and print the energy
            energy = calculate_energy(mass, is_kilograms=(unit_choice == 'kilograms'))
            print(f"The energy corresponding to a mass of {mass} {unit_choice} is {energy} joules.")
    except ValueError:
        print("Invalid input. Please enter a valid number for mass.")

if __name__ == "__main__":
    main()
