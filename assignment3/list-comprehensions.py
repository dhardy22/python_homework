import csv 

with open("../csv/employees.csv", 'r') as file:
    rows = list(csv.reader(file))
    names = [f"{row[1]} {row[2]}" for row in rows[1:]]
    e_list = [ name  for name in names  if "e" in name ] # Case-sensitive on purpose: the spec asks for the letter "e"

print(names)
print(e_list)