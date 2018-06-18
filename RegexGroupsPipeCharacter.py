#Regex Groups and the Pipe character
#Example: Separate an area code from phone number

import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

message = "Call me 415-555-1011 tomorrow, or at 415-555-9999 for office line"
print(message)
print(phoneNumRegex.search(message))
mo = phoneNumRegex.search(message)
print("Now we will do this using the regex search")
print(mo.group())

print("Let's break this Regex up into multiple groups: phoneNumRegex = re.compile(r' (\d\d\d) - (\d\d\d-\d\d\d\d'))")

phoneNumRegex2 = re.compile(r' (\d\d\d)-(\d\d\d-\d\d\d\d) ')
message = "Call me 415-555-1011 tomorrow, or at 415-555-9999 for office line"
print(phoneNumRegex2.search(message))
editedmo = phoneNumRegex2.search(message)


print("Now we'll get the first part of the number")
print(editedmo.group(1))
print("Now we'll get the second part of the number")
print(editedmo.group(2))
print("here's the whole number")
print(editedmo.group())

print("Let's look at the \"|\" character")
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
print("Let's see if we can find something about batman")
bat = batRegex.search('Batmobile lost a wheel')
print(bat.group())
