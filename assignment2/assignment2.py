import csv 
import os
import custom_module
from datetime import datetime


#Task 2
def read_employees():

    empty_dict = {}
    empty_rows = []

    try:
        with open('../csv/employees.csv',mode='r') as file:
            csv_reader = csv.reader(file)

            first_row = True
            for row in csv_reader:
                if first_row:
                    empty_dict["fields"] = row  # Store the header row
                    first_row = False
                else:
                    empty_rows.append(row)  # Append the data rows to the list
            empty_dict["rows"] = empty_rows
        return empty_dict
    except FileNotFoundError:
        print("The file 'employees.csv' was not found.")


employees = read_employees()
print(employees)


#Task 3

def column_index(name):
    if "fields" in employees:
        try:
            index = employees["fields"].index(name)
            return index
        except ValueError:
            print(f"The column '{name}' does not exist in the CSV file.")
    else:
        print("The 'fields' key is missing in the employees dictionary.")

employee_id_column = column_index("employee_id")
employee_lastname_column = column_index("last_name")

print(employee_id_column)
print(employee_lastname_column)  # Example usage of the function

#Task 4

def first_name(row_number):

    if "rows" in employees: #step 1 get the row at position row_number
        if 0 <= row_number < len(employees["rows"]):
            row = employees["rows"][row_number]
            first_name_index = column_index("first_name")
            if first_name_index is not None:
                return row[first_name_index] # step 2 return the value from that row at column_index("first_name")
            else:
                print("The 'first_name' column does not exist.")
        else:            
            print(f"Row number {row_number} is out of range.")

# Task 5

def employee_find(employee_id):
    def employee_match(row):
        return int(row[column_index("employee_id")]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches 

# Task 6

def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

# Task 7

def sort_by_last_name():
    employees["rows"].sort(key=lambda row: row[column_index("last_name")]) 

    column_index("last_name")  # Get the index of the "last_name" column
    return employees["rows"]

print(sort_by_last_name())  # Print the original rows

# Task 8

def employee_dict(row):
    result = {}
    for i in range(len(employees["fields"])):
        key = employees["fields"][i]
        if key == "employee_id":
            continue
        else:
            result[key] = row[i]
    return result

print(employee_dict(employees["rows"][0]))

# Task 9

def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        employee_id = row[column_index("employee_id")]
        result[employee_id] = employee_dict(row)
    return result

print(all_employees_dict())  # Print the dictionary of all employees

# Task 10

def get_this_value():
    THISVALUE = os.getenv("THISVALUE")
    return THISVALUE

# Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
    return custom_module.secret

set_that_secret("new_secret_value")

print(custom_module.secret)  # Output: new_secret_value

# Task 12

def read_csv_file(path):
    data = {}
    rows = []
    
    try:
        with open(path, mode = 'r') as file:
            csv_reader = csv.reader(file)
            first_row = True

            for row in csv_reader:
                if first_row:
                    data["fields"] = row  # Store the header row
                    first_row = False
                else:
                    rows.append(tuple(row))  # Append the data rows to the list
        data["rows"] = rows
        return data
    except Exception as e:
        print(f"An exception occurred: {e}")
        exit()  # Exit the program with a non-zero status to indicate an error

def read_minutes():
    minutes1 = read_csv_file('../csv/minutes1.csv')
    minutes2 = read_csv_file('../csv/minutes2.csv')
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

# Task 13

def create_minutes_set():

    minutes1, minutes2 = read_minutes()
    minutes_set = set()

    for row in minutes1["rows"]:
        minutes_set.add(tuple(row))  # Add each row as a tuple to the set

    for row in minutes2["rows"]:
        minutes_set.add(tuple(row))  # Add each row as a tuple to the set

    return minutes_set

minutes_set = create_minutes_set()

#Task 14

def create_minutes_list():
    minutes_list = list(minutes_set)                       # step 1: set -> list
    converted = map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list)   # step 2: given lambda
    return list(converted)                                 # step 3: map result -> list

minutes_list = create_minutes_list()
print(minutes_list)

def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])  # sort minute_list in ascending order by the second element of each tuple (the date)
    converted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))  # Use map() again to convert each tuple back to (name, date string) with datetime.strftime(date, "%B %d, %Y")

    with open('./minutes.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])  # Write the header row

        for row in converted:
            writer.writerow(row)  # Write each row to the CSV file
    return converted
write_sorted_list()



