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

# Task 8
def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()
    titleized_words = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in little_words:
            titleized_words.append(word.capitalize())
        else:
            titleized_words.append(word.lower())

    return " ".join(titleized_words)

# Task 9
def hangman(secret, guess):
    for letter in secret:
        if letter not in guess:
            secret = secret.replace(letter, "_")
    return secret

# Task 10
def pig_latin(string):
    vowels = "aeiou"
    words = string.split()
    pig_latin_words = []

    for word in words:
        if word[0].lower() in vowels and len(word) > 1:
            pig_latin_words.append(word + "ay")
        else:
            consonant_cluster = ""
            for letter in word:
                if letter.lower() not in vowels:
                    consonant_cluster += letter
                elif letter.lower() == "u" and consonant_cluster.lower().endswith("q"):
                    consonant_cluster += letter   # keep the u with the q
                    break
                else:
                    break
            pig_latin_word = word[len(consonant_cluster):] + consonant_cluster + "ay"
            pig_latin_words.append(pig_latin_word)

    return " ".join(pig_latin_words)

#main line
#if __name__ == "__main__":
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
#     print(student_scores("mean", Tom=75, Dick=89, Angela=91))
#     print(titleize("a tale of two cities in the end"))
# print(hangman("python", "pyth"))
