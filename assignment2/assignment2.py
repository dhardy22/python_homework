import csv 

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