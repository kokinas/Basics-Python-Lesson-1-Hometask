# Task 4.1 wage script
"""
import sys
n, hour, wage, prem = sys.argv
print (f'total wage: {int(hour) * int(wage) + int(prem)}$')
"""

#Task 4.2 transform some list
x = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([y for y in x if y < x [x.index(y) + 1]])

"""
# Task 4.3 multiple of 20, 21
print([y for y in range(20, 240) if (y % 20 == 0) or (y % 21 == 0)])


# Task 4.4 without repeted number
x = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([i for i in x if x.count(i) == 1])
"""

# Task 4.5 