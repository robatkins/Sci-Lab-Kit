#Distance of Light Calculator

def calculate_light_distance(time_seconds):
    # Speed of light in meters per second
    speed_of_light = 3e8
    
    # Calculate distance using the formula distance = speed * time
    distance = speed_of_light * time_seconds
    
    return distance

def main():
    try:
        # Get user input for time in seconds
        time_seconds = float(input("Enter the time in seconds: "))
        
        # Check if the time is non-negative
        if time_seconds < 0:
            print("Time should be a non-negative value.")
            return
        
        # Calculate the distance light travels
        distance = calculate_light_distance(time_seconds)
        
        # Display the result
        print(f"Light travels approximately {distance:.2f} meters in {time_seconds} seconds.")
    
    except ValueError:
        print("Invalid input. Please enter a valid numerical value for time.")

if __name__ == "__main__":
    main()
