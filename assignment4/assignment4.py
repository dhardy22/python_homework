import pandas as pd

# Task 1.1
data = {
    "Name": ['Alice', 'Bob', 'Charlie'],
    "Age": [25, 30, 35],
    "City": ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data)
# print(task1_data_frame)

# Task 1.2
task1_with_salary = task1_data_frame.copy()

task1_with_salary["Salary"] = [70000, 80000, 90000]

# print(task1_with_salary)

# Task 1.3

task1_older = task1_with_salary.copy()

task1_older['Age'] = task1_older['Age'] + 1

print(task1_older)

# Task 1.4

task1_older.to_csv("employees.csv", index=False)


