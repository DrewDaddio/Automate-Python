#Regex Characters
#Find All Method for Regular Expression objects

import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

resume = ("""Drew Daddio Resume: 904820
3031808508
432f
fda
fda 201-317-2222
real: 555-555-5555
""")

print(resume)
print("Find all the phone numbers in the above")
print(phoneRegex.findall(resume))

print("""Types of common Character Classes
\d: Any numeric digit
\D: Any character that is NOT a numeric digit
\w: any letter, numeric digit or underscore
\W: any character NOT a letter, numeric digit or underscore
\s: Any space, tab, or newline character
\S: Any character that is not a space, tab, or newline
""")

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'

xmasRegex = re.compile(r'\d+\s\w+')
print("We'll do a regex based on: r'\d+\s\w+'")
print(xmasRegex.findall(lyrics))

print("Now we'll do a regex to search for vowels: r'[aeiouAEIOU]'")
vowelRegex = re.compile(r'[aeiouAEIOU]')

print(vowelRegex.findall(lyrics))

print("Now we'll look for double vowels in: lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'")
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall(lyrics))
