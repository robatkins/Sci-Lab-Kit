#Rocket Mass and Distance Calculator (For given fuel)
#Methane (CH₄) Specific Impulse: Around 320 seconds
#Refined Kerosene (RP-1) Specific Impulse: Around 311 seconds
#Liquid Oxygen (LOX) Specific Impulse: Around 360 seconds

def calculate_mass_moved(oxidizer_specific_impulse, fuel_specific_impulse, amount_of_fuel):
    gravitational_constant = 9.81  # m/s^2, acceleration due to gravity on Earth

    # Calculate the mass that can be moved using the rocket equation
    mass_moved = (oxidizer_specific_impulse + fuel_specific_impulse) * amount_of_fuel / gravitational_constant

    return mass_moved


def calculate_distance_moved(oxidizer_specific_impulse, fuel_specific_impulse, amount_of_fuel):
    # Calculate the distance moved using the kinematic equation
    total_specific_impulse = oxidizer_specific_impulse + fuel_specific_impulse
    distance_moved = 0.5 * total_specific_impulse * (amount_of_fuel ** 2)

    return distance_moved


def main():
    # Get user input for specific impulses and amount of fuel
    oxidizer_specific_impulse = float(input("Enter the oxidizer specific impulse in seconds: "))
    fuel_specific_impulse = float(input("Enter the fuel specific impulse in seconds: "))
    amount_of_fuel = float(input("Enter the amount of fuel in kilograms: "))

    # Calculate the mass and distance that can be moved
    mass_moved = calculate_mass_moved(oxidizer_specific_impulse, fuel_specific_impulse, amount_of_fuel)
    distance_moved = calculate_distance_moved(oxidizer_specific_impulse, fuel_specific_impulse, amount_of_fuel)

    # Display the results
    print(f"The amount of mass that can be moved is approximately {mass_moved:.2f} kilograms.")
    print(f"The distance that can be moved is approximately {distance_moved:.2f} meters.")


if __name__ == "__main__":
    main()
