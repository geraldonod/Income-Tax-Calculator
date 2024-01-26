#ask user for income value
user_income = float(input("Enter the taxable income: "))
user_tax_payable = 0

print("Given income:", user_income)

#if-else statements to identify interest rate
if user_income <= 10000:
    user_tax_payable = 0
elif user_income <= 20000:
    x = user_income - 10000
    user_tax_payable = x * 10 / 100
else:
    user_tax_payable = 10000 * 10 / 100
    user_tax_payable += (user_income - 20000) * 20 / 100

#print result
print("Total tax to pay is", user_tax_payable)