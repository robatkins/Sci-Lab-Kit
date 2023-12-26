def calculate_feed_amount(chickens, months):
    # Assuming 7.5 pounds of feed per chicken per month
    feed_per_chicken_per_month = 7.5
    total_feed_needed = chickens * feed_per_chicken_per_month * months
    return total_feed_needed

def main():
    # Get user input for the number of chickens and duration in months
    try:
        chickens = int(input("Enter the number of chickens: "))
        months = int(input("Enter the duration in months: "))
        
        # Check if the inputs are valid (positive integers)
        if chickens <= 0 or months <= 0:
            print("Please enter valid positive integers for the number of chickens and duration.")
        else:
            total_feed = calculate_feed_amount(chickens, months)
            print(f"\nTotal amount of feed needed for {chickens} chickens over {months} months: {total_feed} pounds.")
    
    except ValueError:
        print("Please enter valid integers for the number of chickens and duration.")

if __name__ == "__main__":
    main()
