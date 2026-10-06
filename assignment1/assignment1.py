import argparse

#Task 1
def hello():
    return "Hello!"

#Task 2
def greet(name):
    return f"Hello, {name}!"

#Task 3
def calc(num1, num2, operation="multiply"):
    if operation == "multiply":
        try:
            return num1 * num2
        except TypeError:
            return "You can't multiply those values!"

    elif operation == "divide":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "You can't divide by 0!"

    elif operation == "add":
        try:
            return num1 + num2
        except TypeError:
            return "You can't add those values!"

    elif operation == "subtract":
        try:
            return num1 - num2
        except TypeError:
            return "You can't subtract those values!"

    elif operation == "modulo":
        try:
            return num1 % num2
        except ZeroDivisionError:
            return "You can't divide by 0!"

#Task 4
def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        else:
            return f"Invalid data type: {data_type}"
    except ValueError:
        return f"You can't convert {value} into a {data_type}."

#Task 5
def grade(*args):
    try:
        average = sum(args) / len(args)
    except Exception:
        return "Invalid data was provided."

    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

#Task 6
def repeat(string, count):
    result = ""

    for i in range(count):
        result += string 
    return result

#Task 7
def student_scores(statistic, **kwargs):
    if statistic == "mean":
        return sum(kwargs.values()) / len(kwargs)
    elif statistic == "best":
        return max(kwargs, key=kwargs.get)
    else:
        return f"Invalid statistic: {statistic}"
#main line

if __name__ == "__main__":
#     print(hello())
#     print(greet("James"))
#     print(calc(5,6))
#     print(calc(5,6,"add"))
#     print(calc(20,5,"divide"))
#     print(calc(14,2.0,"multiply"))
#     print(calc(12.6, 4.4, "subtract"))
#     print(calc(9,5, "modulo"))
#     print(calc(10,0,"divide"))
#     print(calc("first", "second", "multiply"))
#     print(data_type_conversion("123", "int"))
#     print(grade("three", "blind", "mice"))
#     print(grade(95, 88, 92))         # A
#     print(grade(72, 65, 80))         # C
#     print(grade(40, 55))             # F
#     print(grade("three", "blind"))   # Invalid data was provided.
#     print(repeat("up", 4))
    print(student_scores("mean", Tom=75, Dick=89, Angela=91))
