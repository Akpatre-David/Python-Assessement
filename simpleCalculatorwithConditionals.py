num1 = int(input("Enter num: "))
num2 = int(input("Enter a num: "))

operation = input("Choose an operation (addition, subtraction, multiplication, division): ").strip().lower()

if operation == "addition":
    result = num1 + num2
    print(f"The addition of {num1} and {num2} is {result}")

elif operation == "subtraction":
    result = num1 - num2
    print(f"The subtraction of {num1} and {num2} is {result}")

elif operation == "multiplication":
    result = num1 * num2
    print(f"The multiplication of {num1} and {num2} is {result}")

elif operation == "division":
    if num2 == 0:
        print("Division by zero is not allowed")
    else:
        result = num1 / num2
        print(f"The division of {num1} and {num2} is {result}")

