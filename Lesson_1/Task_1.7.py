#Home task Basics python
###Lesson #1

# Task #1.7 sportsmens goal
print("Task #1.7 sportsmens goal")
numb_kilo = int(input("type the first day result: "))
final_numb = int(input("type the final goal: "))
day = 1
while numb_kilo < final_numb:
	numb_kilo *= 1.1
	day += 1
print(f"The goal will be reached on {day}-th day")