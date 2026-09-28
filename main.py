#taking the input from the user
a = int(input("Enter a number: "))
operation = input("Enter an operation (+, -, *, /): ")
b = int(input("Enter another number: "))

#performing the operation based on user input
if operation == '+':
    result = a + b
    print("The result is:", result)

elif operation == '-':
    result = a - b
    print("The result is:", result)

elif operation == '*':
    result = a * b
    print("The result is:", result)

elif operation == '/':
    if b != 0:
        result = a / b
        print("The result is:", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operation.")