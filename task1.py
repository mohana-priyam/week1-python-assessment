def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)

    if "cap" in options:
        result = min(result, options["cap"])

    return result


print(bonus(50000))
print(bonus(50000, 0.1, 500, 1000))
print(bonus(50000, 0.1, 500, 1000, cap=5000))

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"Name: {self.name}, Salary: {self.salary}, "
            f"Team size: {self.team_size}"
        )


emp = Employee("Rahul", 60000)
print(emp.annual_salary())
print(emp.get_details())

manager = Manager("Divya", 75000, 5)
print(manager.get_details())

class InvalidSalaryError(Exception):
    pass


class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(
                f"Invalid salary: {salary}"
            )

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


try:
    emp = Employee("Test", -500)

except InvalidSalaryError as error:
    print(f"Error: {error}")

finally:
    print("Transaction finished")

import csv

with open("employees.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    employees = [
        {
            **row,
            "salary": int(row["salary"])
        }
        for row in reader
    ]

above_50000 = [
    employee["name"]
    for employee in employees
    if employee["salary"] > 50000
]

print("Above 50000:", above_50000)

# Add a 10% raise using map and lambda
raised_salaries = list(
    map(lambda employee: employee["salary"] * 1.10, employees)
)

print("Raised salaries:", raised_salaries)

# Keep only employees from Chennai
chennai_employees = list(
    filter(
        lambda employee: employee["city"] == "Chennai",
        employees
    )
)

print("Chennai:", [
    employee["name"] for employee in chennai_employees
])

salaries = [30000, 0, 45000, 60000, 75000, 90000, 68000]

for salary in salaries:
    if salary == 0:
        continue

    if salary > 85000:
        print("First salary above 85000:", salary)
        break

    print("Processing salary:", salary)