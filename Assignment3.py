def square_and_multiply(x, y, n):
    # Ensure the base x is in the range [0, n-1]
    x = x % n
    result = 1

    while y > 0:
        if y % 2 == 1:  # If the current bit of y is 1
            result = (result * x) % n
        y = y // 2  # Right shift y (divide by 2)
        x = (x * x) % n  # Square x and reduce modulo n

    return result

def get_integer_input(value):
    while True:
        try:
            value = int(input(value))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def main():
    print("Modular Exponentiation using Square-and-Multiply Algorithm")

    # Get user input with error handling
    x = get_integer_input("Enter the base (x): ")
    y = get_integer_input("Enter the exponent (y): ")
    n = get_integer_input("Enter the modulus (n): ")

    # Check for non-positive modulus
    if n <= 0:
        print("The modulus (n) must be a positive integer. Please try again.")
        return

    # Perform the calculation
    result = square_and_multiply(x, y, n)

    # Display the result
    print(f"The result of {x}^{y} mod {n} is: {result}")

if __name__ == "__main__":
    main()
