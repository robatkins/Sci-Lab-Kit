def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num

def print_sequential_primes(start, count):
    primes = []
    
    while count > 0:
        if is_prime(start):
            primes.append(start)
            count -= 1
        start = find_next_prime(start)
    
    print(f"Sequential prime numbers starting from {start_number}: {primes}")

if __name__ == "__main__":
    try:
        start_number = int(input("Enter the starting number: "))
        count_primes = int(input("Enter the number of sequential prime numbers to print: "))
        
        if start_number <= 0 or count_primes <= 0:
            print("Please enter positive integers for both inputs.")
        else:
            print_sequential_primes(start_number, count_primes)
    
    except ValueError:
        print("Please enter valid integers.")
