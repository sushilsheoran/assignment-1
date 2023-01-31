tax_rate = 0.2
s_deduction = 10000
d_deduction = 3000
gross_income = float(input("Enter your salary: "))
no_of_dependents = int(input("Enter the no. of dependents: "))
Taxable_income = gross_income - s_deduction -(d_deduction*no_of_dependents)
print("Your taxable income: ",Taxable_income)
Tax = Taxable_income*tax_rate
print("Your income tax: ",Tax)