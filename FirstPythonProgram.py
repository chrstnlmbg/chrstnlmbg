import sys

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as error:
        print(f'Invalid Arithmetic Expression: \nValid Sample: 1 + 1 \n\nError Details: {error}')

print("Python Version")
print(sys.version, "\n")

print("Version Info.")
print(sys.version_info, "\n")

while True:
    print("\nInput Arithmetic Expression (or type 'exit' to quit)")
    user_input = input(">> ")
    
    if user_input.lower() == 'exit':
        break
    
    result = calculate(user_input)
    if result is not None:
        print(f"{user_input} is {result}")
        