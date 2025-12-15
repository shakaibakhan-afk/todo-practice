def add(a, b):
    return a + b

def calculator():
    print("Simple Addition Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = add(num1, num2)
    print(f"The result of {num1} + {num2} is: {result}")

# Run the calculator
calculator()
