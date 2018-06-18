#Repetition in Regex Patterns

import re
print("?")
batRegex = re.compile(r'Bat(wo)?man')
adv = "The adventures of Batman"
adv2 = "The adventures of Batwoman"
print(adv)
print(adv2)

mo = batRegex.search(adv)
print(mo.group())

mo2 = batRegex.search(adv2)
print(mo2.group())


phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
message = "Call me 415-555-1011 tomorrow, or at 415-555-9999 for office line"
print(message)
print(phoneRegex.search(message))

print("*: Regular expression context is to match zero or more times")

newbatRegex = re.compile(r'Bat(wo)*man')
print(newbatRegex.search("the adventures of Batwowowowowowoman"))


#match a specific # of repetitions
haRegex = re.compile(r'(Ha)(3)')

print(haRegex.search('He said "HaHaHa"'))
print("Need to figure the above out")

longPhoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d)(,)?(3)')
print("Search: 'My numbers are 415-555-1234, 123-456-7890, 555-212-0000'")
print(longPhoneRegex.search('My numbers are 415-555-1234, 123-456-7890, 555-212-0000'))
print("Need to figure the above out")

digiRegex = re.compile(r'(\d)(3,5)')
digiRegex.search('1234567890')
print(digiRegex.search('1234567890'))
