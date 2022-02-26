# Calculator

# Step 1: Define all the operations in their respective functions.

def sum_it(a, b):
    result = a + b
    return result


def subtract_it(a, b):
    result = a - b
    return result


def multiply_it(a, b):
    result = a * b
    return result


def divide_it(a, b):
    result = a / b
    return result




run_the_program = True
while run_the_program:
    # Step 2: Take User input for the operation to perform
    user_input = input("Please choose what operation you need to perform: +, -, *, /, Exit:")

    # Step 3: Link each operator to it's defined function for the output

    # Step 3.1: Link '+' with sum_it() and take user input for numbers
    if user_input == '+':
        a, b = input("Enter two numbers separated by comma or ',' :").split(',')
        a = int(a)
        b = int(b)
        result = sum_it(a, b)
        print("Addition of a =", a, ",b =", b, "is ", result)


    # step 3.2: Link '-' with subtract_it() and take user input for numbers
    elif user_input == '-':

        a, b = input("Enter two numbers separated by comma or ',' :").split(',')
        a = int(a)
        b = int(b)
        result = subtract_it(a, b)
        print("Subtraction of a=", a, ",b=", b, "is ", result)


    # step 3.3: Link '*' with multiply_it() and take user input for numbers
    elif user_input == '*':

        a, b = input("Enter two numbers separated by comma or ',' :").split(',')
        a = int(a)
        b = int(b)
        result = multiply_it(a, b)
        print("Multiplication of a=", a, ",b=", b, "is ", result)


    # Step 3.4: Link '/' with divide_it() and take user input for numbers
    elif user_input == '/':

        a, b = input("Enter two numbers separated by comma or ',' :").split(',')
        a = int(a)
        b = int(b)
        result = divide_it(a, b)
        print("Division of a=", a, ",b=", b, "is ", result)

    # Step 4: Put a user input to break out of the program

    elif user_input == 'Exit' or user_input == 'exit':
        print("Quit!")
        run_the_program = False