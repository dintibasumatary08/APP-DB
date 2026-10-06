import csv

try:
    file = open("employees.csv", "r")
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