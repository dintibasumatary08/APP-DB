import csv
import os

filename = "employees.csv"

# Create CSV file if it does not exist
if not os.path.exists(filename):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Name", "Monthly Salary"])
        writer.writerow(["Rahul", 45000])
        writer.writerow(["Priya", 60000])
        writer.writerow(["Amit", 52000])
        writer.writerow(["Neha", 40000])

try:
    file = open(filename, "r", encoding="utf-8")
    reader = csv.DictReader(file)

    for employee in reader:
        name = employee["Name"]
        monthly_salary = float(employee["Monthly Salary"])

        annual_salary = monthly_salary * 12

        print("Name:", name)
        print("Monthly Salary:", monthly_salary)
        print("Annual Salary:", annual_salary)

        if monthly_salary > 50000:
            print("Above ₹50,000")
        else:
            print("₹50,000 or below")

        print("--------------------")

    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except ValueError:
    print("Error: Invalid salary value.")

except Exception as e:
    print("Error:", e)