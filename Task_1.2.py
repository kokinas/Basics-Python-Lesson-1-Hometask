#Home task Basics python
###Lesson #1
# Task #1.2 seconds convert to format hh:mm:ss:

print('Task #1.2 seconds convert to format hh:mm:ss ')
val_sec = int(input('type value seconds and I will convert it to format hh:mm:ss '))
hours = val_sec // 3600
minits = (val_sec % 3600) // 60
seconds = val_sec % 60
print('Do not thanks leather bag: %02i:%02i:%02i' %(hours, minits, seconds))
