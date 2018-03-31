spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam)
print(spam.index('hello'))
#index method returns the value of the order that you found the item in the search
# in the index. In the above example
# the value returned should be 0 as the hello was first in the spam list
print('ouput above should be: 0')

print(spam.index('heyas'))
print('ouput above should be: 3')

#append() list method adds the value to the end of the list
test = ['cat',  'dog', 'bat']
print(test)
print("Let's add 'Moose' to this list!")
test.append('Moose')
print(test)

trash = ['bye', 'later', 'cya']
print(trash)
print("Let's add 'goodbye' after 'bye' to this list!")
trash.insert(1, 'goodbye')
#The first part is the position of the item to insert, the second part is the item to insert
print(trash)
print("Now let's try to remove 'cya'")
trash.remove('cya')
print(trash)

#to sort integers use sort()
numbers = [1, 9, 8, 22, 12]
print(numbers)
print("Let's sort these numbers")
numbers.sort()
print(numbers)
#Let's sort these words
print('Lets sort the order of these words by aphabetical order')
print(test)
test.sort()
print(test)

#sorting happens in ASCII-betical order
#so sorting will be from the uppercase letters first to the lower case
alphabet = ['A', 'b', 'C', 'd', 'a', 'B', 'c', 'D']
print(alphabet)
print('now lets sort these using the regular sort without any additional items')
alphabet.sort()
print(alphabet)
print('Now lets sort using "sort(key=str.lower)"')
alphabet.sort(key=str.lower)
print(alphabet)
