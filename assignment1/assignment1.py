#Task 1
def hello():
    return "Hello!"

#Task 2
def greet(name):
    return f"Hello, {name}!"

#Task 3
def calc(num1, num2, operation="multiply"):
    if operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "You can't divide by 0!"


