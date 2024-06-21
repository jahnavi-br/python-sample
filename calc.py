# A basic Python program

# Function to greet the user
def greet(name):
    return f"Hello, {name}!"

# Main function
def main():
    # Prompt the user for their name
    name = input("Enter your name: ")
    
    # Greet the user
    greeting = greet(name)
    print(greeting)
    
    # Perform a simple arithmetic operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Calculate the sum
    sum_result = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum_result}")

# Entry point of the program
if __name__ == "__main__":
    main()
