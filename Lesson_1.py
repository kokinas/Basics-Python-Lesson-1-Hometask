#Home task Basics python
###Lesson #1
print('-'*100)

# Task #1.1 play with varribles:
print('Task #1.1 play with varribles:')
a = input ('type some first numb: ')
b = input ('type some second numb: ')
c =int(a)**int(b)
print(f'first numb is {a}, second numb is {b}, a^b = {c}')
print('-'*100)

# Task #1.2 seconds convert to format hh:mm:ss:
print('Task #1.2 seconds convert to format hh:mm:ss ')
val_sec = int(input('type value seconds and I will convert it to format hh:mm:ss '))
hours = val_sec // 3600
minits = (val_sec % 3600) // 60
seconds = val_sec % 60
print('Do not thanks leather bag: %02i:%02i:%02i' %(hours, minits, seconds))
print('-'*100)

# Task #1.3.1 n + nn + nnn?
print('Task #1.3.1 n + nn + nnn?')
n = input('type a numb, I will calculate n + nn + nnn: ')
print(f'result: {int(n) + int(2 * n) + int(3 * n)}')
# Lesson #1.3.2 n + nn + nnn?
n = input('type a numb, I will calculate n + nn + nnn: ')
print (f'result: {123 * int(n)}')
print('-'*100)

# Task #1.4 max digit
print('Task #1.4 max digit')
numb = int(input('type a number I will show max digit: '))
max = 0
while numb:
	if max < (numb % 10):
		max = numb % 10
	numb = numb // 10
print(f'max digit is {max}')
print('-'*100)


# Task #1.5 income, expanses, revenue.
print('Task #1.5 income, expanses, revenue')
income = int(input('type your income: '))
expanses = int(input('type your expanses: '))
revenue = income - expanses
if revenue > 0: 
	print(f"your revenue is positive and amaunts {revenue}") 
elif revenue == 0:
	print(f"your income and expanses is absolutly equel")
elif revenue < 0:
	print(f"your income is less then expanses on {(-1) * revenue}")
print('-'*100)

#Task #1.6 profitability
print('Task #1.6 profitability')
staff = int(input('type amount of staff: '))
if revenue > 0: 
	print(f"your profitability is {revenue/income}") 
inc_to_staff = income / staff
print(f"each employee income {inc_to_staff}")

# Task #1.7 sportsmens goal
print("Task #1.7 sportsmens goal")
numb_kilo = int(input("type the first day result: "))
final_numb = int(input("type the final goal: "))
day = 1
while numb_kilo <final_numb:
	numb_kilo *= 1.1
	day += 1
print(f"The goal will be reached on the {day}-th day")
