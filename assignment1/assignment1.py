#Task 1
def hello():
    return "Hello!"

if __name__ == "__main__":
    print(hello())

#Task 2
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("James"))

#Task 3
def calc(num1, num2, operation="multiply"):
    if operation == "multiply":
        try:
            return num1 * num2
        except TypeError:
            return "You can't multiply those values!"
    elif operation == "add":
        try:
            return num1 + num2
        except TypeError:
            return "You can't add those values!"
    elif operation == "subtract":
        return num1 - num2
    elif operation == "divide":
        try:
            return num1 / num2
        except TypeError:
            return "You can't divide by 0!"
