#lists and strings are different as lists are mutable while strings are immutable
#create new strings by creating slices
name = 'Zophie a cat'
print(name)
print('let"s slice now')
newName = name[0 : 7] + 'the' +name[8 : 12]
print(newName)

#example of splicing a string vs splicing a list
#reassigning string
spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)

#Now lets reassign a list
spam = [0, 1, 2, 3, 4, 5]
print(spam)
cheese = spam
cheese[1] = 'Hello'
print(cheese)
print("spam should also be changed")
print(spam)
