#Home task Basics python
###Lesson #2

'''
#Task #2.1 script type
list_1 = [1, "Hello", "3", {7 : "3", "1" : "hu"}, range(1,5), (2, 3), ["hi", "wow", 43]]

for el in list_1:
	print(type(el))


#Task #2.2 script type
len_list = int(input("type numb elements of list: "))
list_1 = []

for i in range(1, len_list + 1):
	list_1.append(input(f"type element #{i}: "))
print(list_1)

for i in range(1, len_list, 2):
	buf = list_1[i - 1]
	list_1[i - 1] = list_1[i]
	list_1[i] = buf
print(list_1)

#Task #2.3.1 month season
month = int(input("type numb of month: "))
months = [None, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
seasons = [None, 'winter', 'winter', 'spring',
		   'spring', 'spring', 'summer', 'summer',
		   'summer', 'autumn', 'autumn', 'autumn',
		    'winter']
print(months[month])
print(seasons[month])

#Task #2.3.2 month season
month =input("type numb of month: ")
seasons = {
	 '1' : 'winter',
	 '2' : 'winter',
	 '3' : 'spring',
	 '4' : 'spring',
	 '5' : 'spring',
	 '6' : 'summer',
	 '7' : 'summer',
	 '8' : 'summer',
	 '9' : 'autumn',
	'10' : 'autumn',
	'11' : 'autumn',
	'12' : 'winter'
}
print(seasons[month])

#Task #2.4 split and handle message
in_str = input('type some message')
str_handled = in_str.split()
for i, word in enumerate(str_hendled, 1):
	print(i, word[:10])
'''
#Task #2.5 rating insert
input_numb = int("1")
rating_list = [7, 5, 5, 4, 3, 3, 3, 2]
print(rating_list)
for i in range(0, len(rating_list) - 1):
	if input_numb > rating_list[i]:
		rating_list.insert(i, input_numb)
		break
	elif 
print(rating_list)

