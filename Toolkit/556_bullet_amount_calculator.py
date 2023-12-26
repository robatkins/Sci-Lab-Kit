# Constants
GRAINS_PER_POUND = 7000
GRAINS_PER_BULLET = 70
BULLETS_PER_BOX = 20
SELLING_BOX_PRICE = 20.00
COST_OF_GUNPOWDER = 50.00  # per pound

# Function to calculate the number of bullets
def calculate_bullets(gunpowder_pounds):
    total_grains = gunpowder_pounds * GRAINS_PER_POUND
    bullets = total_grains // GRAINS_PER_BULLET
    return bullets

# Function to calculate the number of boxes
def calculate_boxes(bullets):
    boxes = bullets // BULLETS_PER_BOX
    return boxes

# Function to calculate the revenue from selling the boxes
def calculate_revenue(boxes):
    revenue = boxes * SELLING_BOX_PRICE
    return revenue

# Main function
def main():
    try:
        # User input for the amount of gunpowder in pounds
        gunpowder_pounds = float(input("Enter the amount of gunpowder in pounds: "))

        # Check if the input is non-negative
        if gunpowder_pounds < 0:
            raise ValueError("Gunpowder amount should be non-negative.")

        # Calculate the number of bullets
        bullets = calculate_bullets(gunpowder_pounds)

        # Calculate the number of boxes
        boxes = calculate_boxes(bullets)

        # Calculate the revenue from selling the boxes
        revenue = calculate_revenue(boxes) - (COST_OF_GUNPOWDER * gunpowder_pounds)

        # Display the results
        print(f"With {gunpowder_pounds} pounds of gunpowder, you can produce approximately {bullets} 5.56mm bullets.")
        print(f"This would result in approximately {boxes} boxes of 20 bullets each.")
        print(f"The potential revenue from selling the boxes would be ${revenue:.2f}.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Execute the main function if the script is run
if __name__ == "__main__":
    main()
