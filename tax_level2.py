import tax_level1
standard_deduction = 50000
taxable_income = tax_level1.annual_gross_salary - standard_deduction

print('Gross  Salary',tax_level1.annual_gross_salary)
print('Standard Deduction',standard_deduction)
print('Taxable Income',taxable_income)