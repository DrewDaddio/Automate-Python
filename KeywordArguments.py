print('Hello')
print('World')

# adding  a keyword argument will get "Hello World" on the same line.

print('Hello', end=' ')
print('World')
# the "end=' '" adds a single space character at the end of Hello starts the next print right next ot it

print('cat', 'dog', 'mouse')
#the above will have a single space character
print('cat', 'dog', 'mouse', sep='ABC')
#the above "sep" argument will make ABC show in the spaces instead of a single space character
