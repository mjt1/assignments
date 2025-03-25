# Simple Calculator Program

def calculate(num1, num2, operator):
    """Perform calculation based on the operator"""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Check for division by zero
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"

def main():
    # Get user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operation (+, -, *, /): ")
        
        # Perform calculation
        result = calculate(num1, num2, operator)
        
        # Display result
        if isinstance(result, str):
            print(result)
        else:
            print(f"{num1} {operator} {num2} = {result}")
            
    except ValueError:
        print("Error: Please enter valid numbers")

if __name__ == "__main__":
    main()