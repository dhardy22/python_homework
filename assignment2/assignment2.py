import csv 


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


