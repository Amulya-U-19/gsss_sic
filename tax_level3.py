import tax_level2 as t2
section_87A_rebate=True

tax_percentage
if t2.taxable_income>=0 and t2.taxable_income<3_00_000:
    pass
elif t2.taxable_income<=6_00_000:
    tax_percentage=.05
elif t2.taxable_income<=9_00_000:
    tax_percentage=.10
elif t2.taxable_income<=12_00_000:
    tax_percentage=.15
elif t2.taxable_income<=15_00_000:
    tax_percentage=.2

print(f'cess amount      =  {cess_amount}')
print(f'total tax amount = {total_tax_amount}')