#Home task Basics python
###Lesson #3 FUNCTION
'''
#Task #3.1 divide function
def divide(divident, divisor):
	"""
	first number divid by second

	(number, number) -> number

	>>> divide(99, 11)
	9
	"""
	try:
		return divident/divisor
	except:
		return "cannot be divided by zero"
print(divide(10, 0))
print("that's all")


#Task #3.2 print user data
def print_user_data(name, surname, birthday, town, email, tele_num):
	"""
	make sentense with users data

	(string, string, string, string, string, string, string) -> string

	>>> print_user_data('Ivan', 'Ivanov', '01.01.1990', 'Moscow', 'ivanovII@gmail.com', '+79999879898')

	"Ivan Ivanov 01.01.1990 Moscow ivanovII@gmail.com +79999879898"

	"""
	return('{} {} {} {} {} {}'.format(name, surname, birthday, town, email, tele_num))

print (print_user_data('Ivan', 'Ivanov', '01.01.1990', 'Moscow', 'ivanovII@gmail.com', '+79999879898'))


#Task #3.3 sum two maximum

def sum_max(numb1, numb2, numb3):
	"""
	return sum of two maximum number

	(number, number, number) -> number

	>>> sum_max(3, 8, 4)
	12
	"""
	list1 = [numb1, numb2, numb3]
	list1.remove(min(list1))
	return sum(list1)

print (sum_max(3, 8, 3))


#Task #3.4.1 exponentiation
def exp1(x, y):
	"""
	#return x exponent negative y

	(number, number) -> number
	
	exp(4, -4)
	256
	"""

	if y < 0:
		y = (-1) * y
	else:
		return "'y' must be positive number"
	return (x**y)

print (exp1(4, -4))

#Task #3.4.2 exponentiation
def exp2(x, y):
	"""
	#return x exponent negative y

	(number, number) -> number
	
	exp(4, -4)
	256
	"""

	result = x
	if y < 0:
		y = (-1) * y
	else:
		return "'y' must be positive number"
	for i in range(y - 1):
		result = result * x
	return result

print (exp2(4, -4))
'''

#Task #3.5