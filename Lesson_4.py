

#Task #4.1 function salary of employee
def calc_wage(hour, wage, prem):
	"""
	calculete total wage of employee

	(number, number, number) -> number

	>>> calc_wage(1000, 5, 200)
	5200
	"""
	return hour * wage + prem

print(calc_wage(1000, 5, 200))
print(calc_wage(924, 633, 22100))