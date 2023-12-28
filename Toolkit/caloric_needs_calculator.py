def calculate_caloric_needs(num_humans, num_days):
    # Constants for daily caloric needs per person
    caloric_needs_per_person = 2000  # you can adjust this value based on your requirements

    # Calculate total caloric needs for the population and specified number of days
    total_caloric_needs = num_humans * caloric_needs_per_person * num_days

    return total_caloric_needs

def main():
    # Get the number of humans and number of days from the user
    try:
        num_humans = int(input("Enter the number of humans: "))
        num_days = int(input("Enter the number of days: "))
        
        # Ensure the inputs are non-negative
        if num_humans < 0 or num_days < 0:
            raise ValueError("Number of humans and number of days must be non-negative.")

        # Calculate and display the total caloric needs
        total_caloric_needs = calculate_caloric_needs(num_humans, num_days)
        print(f"The total caloric needs for {num_humans} humans over {num_days} days is approximately {total_caloric_needs:.2f} calories.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
