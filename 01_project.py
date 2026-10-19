employees = [
    {"id": 1, "name": "Amit", "salary": 50000, "city": "Delhi"},
    {"id": 2, "name": "Rahul", "salary": 65000, "city": "Mumbai"},
    {"id": 3, "name": "Suresh", "salary": 45000, "city": "Delhi"},
    {"id": 4, "name": "Amit", "salary": 75000, "city": "Pune"},
    {"id": 5, "name": "Suresh", "salary": 60000, "city": "Mumbai"}
]

# for emp in employees:
#     if emp["salary"]>55000:
#        print(employees)


# result = [(employees["name"],employees["salary"]) for employees in employees]
# for name,salary in result:
#     print(name,salary)


# # find second highest salary
# max_salary = max(emp["salary"] for emp in employees)
# print("Max salary:",max_salary)


# highest = 0
# second_highest = 0

# for emp in employees:
#     salary = emp["salary"]

#     if salary > highest:
#         second_highest = highest
#         highest = salary

#     elif salary > second_highest:
#         second_highest = salary

# print("Highest:",highest)
# print("Second Highest salary:",second_highest)

def dublicate(empoyees):
    names =[]

    for emp in employees:
        name = emp["name"]

        if name not in names:
            names.append(name)
            print(name)
dublicate(employees)

names = [emp["name"] for emp in employees]

for name in set(names):
    if names.count(name)>1:
        print("dublicate Name:",name)

for emp in employees:
    if emp["city"] == "Mumbai":
        print(emp["name"],emp["salary"])
