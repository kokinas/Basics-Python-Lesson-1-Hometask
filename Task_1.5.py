#Home task Basics python
###Lesson #1
# Task #1.5 income, expanses, revenue.

print('Task #1.5 income, expanses')
income = int(input('type your income: '))
expanses = int(input('type your expanses: '))

if income > expanses: 
	print(f"your income is positive") 
elif income == expanses:
	print(f"your income and expanses is absolutly equel")
elif income < expanses:
	print(f"your income is less then expanses")

