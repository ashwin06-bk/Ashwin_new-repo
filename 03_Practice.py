name = "Amit"
age = 25
salary = 50000
city = "Pune"
experiance = 2.5 
is_active = True

print("Employee Name:",name)
print("Age:",age)
print("Salary:",salary)
print("City:",city)
print("Experiance:",experiance)
print("Is_Active:",is_active)

print("Sales Transaction:")

product = "Laptop"
quantity = 3
price = 55000
discount = 5000
total_price = price*quantity

print("Product:",product)
print("Quantity:",quantity)
print("Total Price:",total_price)
print("Discount Price:",total_price-discount)

print()

print("Data Pipeline:")

total_records = 10000
successful_records = 9850
failed_records = 150

successful_records_ratio = successful_records/total_records*100
failed_records_ratio = failed_records/total_records*100

print("Total Records:",total_records)
print("Successful records:",successful_records)
print("Failed Records:",failed_records)

print("Success Ratio:",successful_records_ratio)
print("Failed Ratio:",failed_records_ratio)

print()
print("Company Sales:")

sales = [4500,6800,7500,5000,5800,4000]
average= sum(sales)/len(sales)

print("Toal Sales:",sum(sales))

print("Maximum Sale:",max(sales))
print("Minimum sales:",min(sales))

print("length sale:",len(sales))

print("Average sale:",average)

print()

print("Company Salaries:")

salaries = [46000,50060,36500,54000,60000]
