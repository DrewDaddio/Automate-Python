#list data values
spam = ['cat', 'bat', 'rat', 'elephant']
#lists are comma delimited and start/end with brackets
print('show spam[0]: ' + spam[0])
print(spam[0])
print('show spam[1]: ' + spam[1])
print(spam[1])
print('show spam[2]: ' + spam[2])
print(spam[2])
print('show spam[3]: ' + spam[3])
print(spam[3])

ulti = [['Cat', 'Bat', 'Rat', 'Mouse'], [10, 20, 30, 40]]
print(ulti)
#This output will print out the list values of the first list
print(ulti[0])
#this output will print out a specific item within the list of the list
print(ulti[0][0])

#this will print the last item in the spam list
print('this will print the last item in the spam list')
print(spam)
print(spam[-1])

numbers = [10, 20, 30]
#you can change values in a list
print(numbers)
print('Change numbers[1] to hello')
numbers[1] = 'Hello'
print(numbers)
