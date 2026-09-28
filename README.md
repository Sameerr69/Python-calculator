# Python Calculator

A simple command-line calculator built with Python. It takes two numbers and an arithmetic operation from the user and displays the result.

## Features

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`)
* Handles division by zero
* Handles invalid operations
* Takes input directly from the user

## Requirements

* Python 3.x

## How to Run

1. Make sure Python is installed on your computer.
2. Clone or download this repository.
3. Open the project folder in your terminal.
4. Run the Python file:

```bash
python calculator.py
```

## Example

```text
Enter a number: 10
Enter an operation (+, -, *, /): *
Enter another number: 5
The result is: 50
```

## Error Handling

The program prevents division by zero:

```text
Enter a number: 10
Enter an operation (+, -, *, /): /
Enter another number: 0
Error: Division by zero is not allowed.
```

It also displays an error when an invalid operation is entered.

## Technologies Used

* Python


