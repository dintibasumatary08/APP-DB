def report_format(func):
    def wrapper():
        print("\n----- STUDENT ATTENDANCE REPORT -----")
        func()
        print("---------- END OF REPORT ----------")
    return wrapper



class AttendanceReport:
    report_count = 0

    def __init__(self, class_name, date):
        self.class_name = class_name
        self.date = date
        self.students = []     # List of tuples (Name, Status)
        AttendanceReport.report_count += 1

    def add_student(self, name, status):
        self.students.append((name, status))

    def __str__(self):
        return f"Class: {self.class_name}\nDate: {self.date}"

    def __len__(self):
        return len(self.students)

    @classmethod
    def total_reports(cls):
        print(f"\nTotal Attendance Reports Generated: {cls.report_count}")
        
    @report_format
    def display(self, template):
        print(self)
        print("\nTemplate:", template)

        present = 0
        absent = 0

        if template.lower() == "simple":
            print("\nStudent Attendance")
            for name, status in self.students:
                print(f"{name:<20} {status}")

        elif template.lower() == "detailed":
            print("\nDetailed Attendance")
            print("-" * 40)
            print(f"{'Student':<20}{'Status'}")
            print("-" * 40)
            for name, status in self.students:
                print(f"{name:<20}{status}")
                if status.lower() == "present":
                    present += 1
                else:
                    absent += 1

            print("-" * 40)
            print("Present :", present)
            print("Absent  :", absent)

        elif template.lower() == "summary":
            for name, status in self.students:
                if status.lower() == "present":
                    present += 1
                else:
                    absent += 1

            print(f"Total Students : {len(self.students)}")
            print(f"Present        : {present}")
            print(f"Absent         : {absent}")

        else:
            print("Invalid Template")


report = AttendanceReport(
    input("Enter Class Name: "),
    input("Enter Date (DD-MM-YYYY): ")
)

n = int(input("Enter Number of Students: "))

for i in range(n):
    print(f"\nStudent {i+1}")
    name = input("Enter Student Name: ")
    status = input("Attendance (Present/Absent): ")
    report.add_student(name, status)

print("\nChoose Report Template")
print("1. Simple")
print("2. Detailed")
print("3. Summary")

choice = input("Enter Choice: ")

if choice == "1":
    report.display("simple")
elif choice == "2":
    report.display("detailed")
elif choice == "3":
    report.display("summary")
else:
    print("Invalid Choice")

print("\nUsing Magic Method __len__")
print("Total Students in Report:", len(report))

AttendanceReport.total_reports()