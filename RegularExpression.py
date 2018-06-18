#Regular Expressions
#Allow you to specify a pattern of text to search for.

#expression to check for phone number

def isPhoneNumber(text):
    if len(text) != 12:
        return False # not phone number sized
    if text[3] !=  '-':
        return False # missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False # no first 3 digits
        if text[7] != '-':
            return False  # missing last 4 digits
    return True

print(isPhoneNumber('415-555-1234'))
                
message = "Call me 415-555-1011 tomorrow, or at 415-555-9999 for office line"

#to detect where in the string the phone number is
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')


#i is the beginning of the index and then it will go to 12 characters
#Now we will do this in a regular expression to show how it can be condensed

print("This will be done using the Regular Expression method now")
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#regular expressions use a lot of back slashes
# \d = Looking for a digit
# above will look for a pattern of "3 digits - 3 digits - 4 digits"

mo = phoneNumRegex.search(message)
print(mo.group())
print("This got the first pattern of digits")
 
