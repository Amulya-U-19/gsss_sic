employee_name = input('Enter the name of the Empoloyee:')
employee_id = int(input('Enter the id of the Empoloyee:'))
employee_salary = int(input('Enter the salary of the Employee:'))
special_allowance = int(input('Enter the special allowance :'))
bonus_percentage = float(input('Enter the bonus percentage:'))
gross_monthly_salary = employee_salary + special_allowance
annual_gross_salary = (gross_monthly_salary * 12) + bonus_percentage

print('Gross Monthly Salary of an Employee is', gross_monthly_salary)
print('Annual Gross Salary of an Employee is', annual_gross_salary )