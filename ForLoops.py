#For loops and other things
print('the following scripts will do the same exact things')

for i in range(4):
    print(i)

print('this is the other script. Look at the code')
#This is the same thing but different way to do it
for j in [0, 1, 2, 3]:
    print(j)

#can also use the list function to print out the above ranges
print('use list to print out the ranges in list format')
list(range(4))
print(list(range(4)))

#to create a list within a defined range and way to step up
spam = list(range(0, 100, 2))
#the 0 = min, 100 = max, 2 = amount to go up by each time
print(spam)

#this is an example of how to use the for loop 'i" to be able to call an item list and list the item as well
supplies = ['pens', 'staplers', 'flame-throwers',  'binders']
for i in range(len(supplies)):
    print('index ' + str(i) + ' in supplies is: ' + supplies[i])

#Multiple assignment trick
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
print(cat)

#example of switching items together
a = 'aaa'
b = 'bbb'
print('Print a: ' + a)
print('Print b: ' +b)
print('You can use simple instructions to add items from other lists together')
a, b = b, a
print('Print a: ' + a)
print('Print b: ' +b)
