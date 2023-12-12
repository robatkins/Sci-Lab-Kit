def generate_fibonacci_sequence(start, count):
    fibonacci_sequence = []
    a, b = 0, 1
    
    # Find the first Fibonacci number greater than or equal to the starting number
    while a < start:
        a, b = b, a + b
    
    for _ in range(count):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    return fibonacci_sequence

def print_sequential_fibonacci(start, count):
    fibonacci_sequence = generate_fibonacci_sequence(start, count)
    
    print(f"Sequential Fibonacci numbers starting from {start}: {fibonacci_sequence}")

if __name__ == "__main__":
    try:
        start_number = int(input("Enter the starting number for Fibonacci sequence: "))
        count_fibonacci = int(input("Enter the number of sequential Fibonacci numbers to print: "))
        
        if start_number < 0 or count_fibonacci <= 0:
            print("Please enter a non-negative starting number and a positive count.")
        else:
            print_sequential_fibonacci(start_number, count_fibonacci)
    
    except ValueError:
        print("Please enter valid integers.")
