# defining an addition function
def add(num1, num2):
    return num1 + num2


# defining the subtraction function
def subtract(num1, num2):
    return num1 - num2


# defining the multiplication function
def multiply(num1, num2):
    return num1 * num2


# defining the division function
def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by 0")


# This function should create a txt file and write the results to it
def record_calculation(num1, num2, operation, result, filename):
    with open(filename, "a") as file:
        file.write(f"{num1} {operation} {num2} = {result}\n")


# Main calculator function
def calculate():
    filename = "calculator.txt"
    while True:
        try:
            user_num1 = input("Please enter the first number (or 'stop' to exit): ").lower()
            if user_num1 == "stop":
                break
            user_operator = input("Please enter operator (+, -, *, /): ")
            user_num2 = input("Enter second number: ")
            user_num1 = float(user_num1)
            user_num2 = float(user_num2)
            if user_operator == "+":
                result = add(user_num1, user_num2)
            elif user_operator == "-":
                result = subtract(user_num1, user_num2)
            elif user_operator == "*":
                result = multiply(user_num1, user_num2)
            elif user_operator == "/":
                result = divide(user_num1, user_num2)
            else:
                print("Invalid operator")
                continue
            print(f"{user_num1} {user_operator} {user_num2} = {result}")
            record_calculation(user_num1, user_num2, user_operator, result, filename)
            print("Calculation recorded")
        except ValueError:
            print("Invalid input")
        except ZeroDivisionError as e:
            print(e)
            continue
        # expanding the program to review the calculations
        read_record = input("Would you like to view the calculations? (y/n): ").lower()
        if read_record == "y":
            while True:
                try:
                    with open(filename, "r") as file:
                        equations = file.readlines()
                        for equation in equations:
                            parts = equation.split()
                            num1 = float(parts[0])
                            num2 = float(parts[2])
                            operator = parts[1]
                            if operator == "+":
                                result = add(num1, num2)
                            elif operator == "-":
                                result = subtract(num1, num2)
                            elif operator == "*":
                                result = multiply(num1, num2)
                            elif operator == "/":
                                result = divide(num1, num2)
                            else:
                                print("Invalid operator")
                                continue
                            print(f"{num1} {operator} {num2} = {result}")
                    break
                except FileNotFoundError:
                    print("File not found.")
                    continue
        else:
            print("Thank you for using the calculator.")


calculate()

# resources used:
# https://thenewstack.io/yet-more-python-for-beginners-saving-input-to-a-file/
# https://runestone.academy/ns/books/published/py4e-int/files/userNames.html
