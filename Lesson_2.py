#Home task Basics python
###Lesson #2

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

#Task #2.5 rating insert
rating_list = [7, 5, 5, 4, 3, 3, 3, 2]
print(rating_list)
input_numb = int(input('Type a numb to insert to rating list: '))
flag_min = False
for numb in rating_list:
	if numb < input_numb:
		index = rating_list.index(numb)
		rating_list.insert(index, input_numb)
		flag_min = True
		break
if not flag_min:
	rating_list.append(input_numb)
print(rating_list)

#Task #2.6 structer data of goods

data_base = [
(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
(2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
(3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]

#Add new good
max = int(input('type number of adding goods: '))
for i in range(1, max + 1):
	name = input(f'Type name of good #{i}: ')
	price = int(input(f'Type price of good #{i}: '))
	numb = int(input(f'Type numb of good #{i}: '))
	unit = input(f'Type unit of good #{i}: ') 
	count = len(data_base)
	data_base.append((len(data_base) + 1, {'название': name, "цена" : price, 'количество' : numb, 'eд' : unit} ))
	print('adding good complete')

for i in data_base:
	print(i)

output_base = {}
keys = data_base[1][1].keys()		# receive all keys
for key in keys:
	buf = []
	for val in data_base:
		buf.append(val[1].get(key))
	output_base.update({key : buf})
print('{')
for i, j in output_base.items():
	print (f'{i} : {j}')
print('}')
