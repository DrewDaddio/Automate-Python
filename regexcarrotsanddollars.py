#Regex Dot Star & Caret Dollars

# $ at end of the expression: must end with the pattern
# ^ at beginning of the expression: Must start with the pattern

import re

beginsWithHelloRegex = re.compile(r'^Hello')

print(beginsWithHelloRegex.search('Hello world'))

print("The carrot in the beginsWithHelloRegex variable searched for \"Hello World\"")

#now let's do this for digits

AllDigitsRegex = re.compile(r'^\d+$')
#$ searches for the pattern at the end

numberSearch = '25874328572344587'
incorrectSearch = '2a5s8f7f4d3s2f8h5u7o2o3pk4s4c5d8f7'
print(AllDigitsRegex.search(numberSearch))
print("This works because the variable numberSearch is all numbers")
# print("The next search based on the variable incorrectsearch won't work because it's numbers and letters")
# print(AllDigitsRegex.search(IncorrectSearch))

atRegex = re.compile(r'.at')
rhyme = 'The cat in the hat sat on the flat mat'
print(atRegex.findall(rhyme))
print("Flat is matched in our command 're.compile(r'.at')' because the dot character is only looking for a single character before .at")
newAtRegex = re.compile(r'.{1,2}at')
print(newAtRegex.findall(rhyme))
print("Notice now the new command 're.compile(r'.{1,2}at')' shows flat but now it's bringing in an extra white space before the other words")
print("This is where we'll use the * in order to get all the variables")

name = 'First Name: Al Last Name: Sweigart'
print(name)
print(name.find(' : '))
print("name.find(' : ')")

print("name.find(' : ') + 2")
print(name.find(' : ') + 2)

print("name([12: ]")
print(name[12: ])

print("Now we'll do the above using the * regular expression")

print("nameRegex = re.compile(r'First Name:  (.*)  Last Name:  (.*)')")
print("nameRegex.findall( 'First Name: Al Last Name: Sweigart'))")

nameRegex = re.compile(r'First Name:  (.*)  Last Name:  (.*)')
print(nameRegex.findall('First Name: Al Last Name: Sweigart'))

print("I can't get this working for some reason. I'll need to come back ot this")

serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))

greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

prime = 'Serve the public trust. \nProtect the innocent. \nUpload the law.'
print(prime)

dotStar = re.compile(r'.*')
print(dotStar.search(prime))
dotStar2 = re.compile(r'.*', re.DOTALL)
print(dotStar2.search(prime))

vowelRegex = re.compile(r'[aeiou]', re.I)
vowelState = 'Al, why does your programming book talk about RoboCop so much?'
print("vowelRegex = re.compile(r'[aeiou', re.I) \nvowelState = 'Al, why does your programming book talk about RoboCop so much?'")
print(vowelRegex.search(vowelState))
print(vowelRegex.findall(vowelState))
