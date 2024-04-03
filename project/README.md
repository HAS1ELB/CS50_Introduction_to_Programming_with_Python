# Simple Calculator
#### Video Demo: <https://youtu.be/DueU5-hi_yI>
#### Description:

This project is a simple calculator program implemented in Python. The calculator allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

### Files:

1. **project.py**:
    - This file contains the main function `main()` which serves as the entry point of the program.
    - It also includes additional functions:
        - `perform_operation(num1, num2, operation)`: This function takes two numbers and an operation as input and performs the specified arithmetic operation.
        - `add(num1, num2)`: This function adds two numbers.
        - `subtract(num1, num2)`: This function subtracts one number from another.
        - `multiply(num1, num2)`: This function multiplies two numbers.
        - `divide(num1, num2)`: This function divides one number by another.

2. **test_project.py**:
    - This file contains test functions for each of the functions defined in `project.py`.
    - Each test function in this file verifies the correctness of the corresponding function in `project.py` using assertions.

3. **requirements.txt**:
    - This file lists the pip-installable libraries required by the project. Currently, it only includes `pytest`, which is used for testing.

### Design Choices:

- **Separation of Concerns**: I chose to separate the main program logic (`project.py`) from the test logic (`test_project.py`). This separation allows for better organization and makes it easier to maintain and debug the code.

- **Input Validation**: The calculator program validates user input to ensure that it is appropriate for arithmetic operations. For example, division by zero is handled gracefully, and the program returns an appropriate error message in such cases.

- **Use of pytest**: I decided to use the `pytest` library for testing as it provides a simple and intuitive way to write and run tests. Each function in `project.py` has corresponding test functions in `test_project.py`, ensuring that the program's functionality is thoroughly tested.

- **Readability**: I aimed to write clear and readable code with descriptive function and variable names to enhance code readability and maintainability.

- **Documentation**: I included comments within the code to explain the purpose and functionality of each function. Additionally, this README.md file provides an overview of the project structure and design choices.

This simple calculator project demonstrates the basics of Python programming, including defining functions, handling user input, and writing tests for validation. It serves as a foundation for more complex projects and provides a practical example of software development principles.


