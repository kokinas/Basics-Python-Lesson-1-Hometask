#Home task Basics python
###Lesson #3 FUNCTION

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
def print_user_data(name, surname, birthday, town, e-mail, tele_num):
	