# Logging
# Logging is a good way to debug the program
# Creates a trail of actions that we can define.

#This is the setup code to setup loggin
import logging
logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s) - %(message)s')
logging.disable(logging.CRITICAL)
print('There are 5 levels of logging: \n1. Debug\n2. Info\n3. Warning\n4. Error\n5. Critical.')

# example using factorial function to demonstrate logging
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial (%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i # Total multiplied by I
        logging.debug('i is %s, total is %s' % (i, total))
        
    logging.debug('Return  value is %s' % (total))
    return total

print('Let\'s check if the factorial is working. Factorial of 5 = ', factorial(5))
print("Whoops, let's check the log")

print('We\'ve looked at the logs and have updated the \'Factorial\' program')

def factorialNew(n):
    logging.debug('Start of factorialNew (%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i # Total multiplied by I
        logging.debug('i is %s, total is %s' % (i, total))
        
    logging.debug('Return  value is %s' % (total))
    return total

print('Let\'s check if the new factorial is working. Factorial of 5 = ', factorialNew(5))
print('Now we can see it\'s working. You can check if the debug is working by going into the code and commenting out the logging.disable function.') 
print('''We can also change the output of the logging from within python to a text file by changing:

This will put the logging in the python program output:
logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s) - %(message)s')

This will push the logging to the text file named:
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format = '%(asctime)s - %(levelname)s) - %(message)s')
''')

logging.debug('End of Program')
