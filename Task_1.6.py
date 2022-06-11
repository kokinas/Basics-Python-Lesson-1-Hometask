#Home task Basics python
###Lesson #1

#Task #1.6 profitability
print('Task #1.6 profitability')

income = int(input('type your income: '))
expanses = int(input('type your expanses: '))
revenue = income - expanses
if revenue > 0: 
	print(f"your profitability is {revenue/income}") 
staff = int(input('type amount of staff: '))
inc_to_staff = income / staff
print(f"each employee income {inc_to_staff}")

