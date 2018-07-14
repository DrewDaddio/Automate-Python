# Raise and Assert Statements
# How to debug
# Python will raise an exception whenever there are issues in the code

print("You can raise your own exceptions in your code as a way to stop the code in this function and move to the accept statement")
print("Exceptions are raised with the 'Raise' statement")
print("raise Exception('This is the error message.')")

def boxPrint(symbol, width, height):
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + ('  ' * (width)) + symbol)

    print(symbol * width)

boxPrint('*', 15, 5)

def refBoxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + ('  ' * (width)) + symbol)

    print(symbol * width)

# Below will raise exception
# refBoxPrint('**', 15, 5)

def ref2BoxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater or equal to 2.')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + ('  ' * (width)) + symbol)

    print(symbol * width)

# Below will raise exception
#ref2BoxPrint('*', 1, 1)

# the traceback.format_exc() Function
import traceback

# Below will try an exception
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written error_log.txt')

# Assertions and the assert statement
# Assertions are sanity checks on the code

#assert False, 'This is the "Assert" error message.'

market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
        assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

switchLights(market_2nd)
