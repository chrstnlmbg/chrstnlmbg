def myCalculator():
    import re
    
    def is_valid_arithmetic_expression(input_str):
        # Return True if the input string is empty or contains only whitespace
        # or if it consists of one or more digits
        return not input_str.strip() or re.match(r'^\d+$', input_str)
    
    def evaluate_arithmetic_expression(expression):
        try:
            # Using eval can be risky due to potential security issues. 
            # It's generally better to implement your own expression evaluation.
            result = eval(expression)
            return f">> {expression} is {result}"
        except Exception as e:
            # Provide more specific error messages
            return f">> Please provide a valid arithmetic expression."
    
    def print_invalid_expression_message(user_input):
        print(f">> Please provide a valid arithmetic expression.")
    
    def print_empty_input_message():
        print(">> Please provide a valid arithmetic expression.")
    
    def print_welcome_message():
        print("Calculator by Chanix \n>>")
    
    # Print a welcome message to indicate the purpose of the program
    print_welcome_message()
    
    # Start an infinite loop to repeatedly ask for user input
    while True:
        # Prompt the user to input an arithmetic expression
        user_input = input("Input an Arithmetic Expression (or type 'exit' to quit): ")
        
        # If the user types 'exit', exit the loop and end the program
        if user_input.lower() == 'exit':
            break
        
        # Check if the input contains only one integer
        if re.match(r'^\d+$', user_input):
            print_invalid_expression_message(user_input)
            continue
    
        # Check if the input is a valid arithmetic expression
        if is_valid_arithmetic_expression(user_input):
            print_empty_input_message()
            continue
    
        # If the input is a valid expression, evaluate it and print the result
        print(evaluate_arithmetic_expression(user_input))

def pattern_generator():
    # Function to generate patterns based on user input
    pattern_type = input("Enter the pattern type (e.g., diamond, triangle): ")

    if pattern_type == "diamond":
        size = int(input("Enter the size of the diamond: "))
        for i in range(1, size + 1):
            print(" " * (size - i) + "*" * (2 * i - 1))
        for i in range(size - 1, 0, -1):
            print(" " * (size - i) + "*" * (2 * i - 1))
    elif pattern_type == "triangle":
        size = int(input("Enter the size of the triangle: "))
        for i in range(1, size + 1):
            print(" " * (size - i) + "*" * (2 * i - 1))
    else:
        print("Invalid pattern type. Please enter a valid pattern type.")

# Main program
while True:
    print("Chanix Python Programs:")
    print("1. Calculator")
    print("2. Pattern Generator")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == '3':
        break
    elif choice == '1':
        myCalculator()
    elif choice == '2':
        pattern_generator()
    else:
        print("Invalid choice. Please select a valid option.")
