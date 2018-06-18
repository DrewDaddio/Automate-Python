#String Formatting: Section 8 Lecture 21
#OOP

name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'turnips'
print('Hello ' + name + ', you are invited to a party at ' + place + ' at ' + time + '. Please bring ' + food + '.')


#String Formatting aka Strin Interpellation. Le'ts us put a string s which allows to put other string into it.
print('Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food))
