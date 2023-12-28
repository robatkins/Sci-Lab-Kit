def calculate_water_needs(num_humans, num_days):
    # Constants for water needs per person in liters and conversion factor to gallons
    water_needs_per_person_liters = 3.7  # for men; you can adjust this value
    conversion_factor_liters_to_gallons = 0.264172

    # Calculate total water needs for the population and specified number of days
    total_water_liters = num_humans * water_needs_per_person_liters * num_days
    total_water_gallons = total_water_liters * conversion_factor_liters_to_gallons

    return total_water_gallons

def main():
    # Get the number of humans and number of days from the user
    try:
        num_humans = int(input("Enter the number of humans: "))
        num_days = int(input("Enter the number of days: "))
        
        # Ensure the inputs are non-negative
        if num_humans < 0 or num_days < 0:
            raise ValueError("Number of humans and number of days must be non-negative.")

        # Calculate and display the total water needs
        total_water_gallons = calculate_water_needs(num_humans, num_days)
        print(f"The total water needs for {num_humans} humans over {num_days} days is approximately {total_water_gallons:.2f} gallons.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
