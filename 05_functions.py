def annual_salary(monthly_salary):
    return monthly_salary * 12
salary = annual_salary(50000)
print(salary)

# data cleaning

def clean_name(name):
    name = name.strip()
    name = name.capitalize()

    return name
result = clean_name("    ashwin    ")
print(result)

salary1 = [40000,75000,45000,67000,88000]

def get_high_salary(maxsalary):
    high_salary = max(maxsalary)
    return high_salary
result1 = get_high_salary(salary1)
print(result1)