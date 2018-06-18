#String methods return a new string value rather than modify the string in place
# strings are immutable
spam = 'Hello World!'
print(spam)
spam.upper()
print(spam.upper())
# now we will do an example using a case insensitive comparison
print('Yes or no?')
answer = input()
print(answer)
if answer == 'yes':
    print('Playing again')
if answer.isupper() == 'yes':
    print('Playing again')


#now this will make spam lower case
print(spam)
print(spam.lower())

#this will be the type of string returns
print(""" These are the type of string methods:
isalpha() - letters only
isalnum() - letters and numbers only (alphanumeric)
isdecimal() - numbers only
isspace() - whitespace only
istitle() - titlecase only""")

#String return methods:
print("""Here are some more string return methods
startswith() - returns what is started
endswith() - returns with what is ended
join() - joins a list of strings into one string
split() - returns the individual words from a string
rjust() - right justifies
ljust() - left justifies
center() - center justified
strip() - removes the whitespace of a string and returns a new string
lstrip() - removes whitespace from the left side
rstrip() - removes whitespace from the right side.
replace() - takes 2 arguments. String to look for and string to replace it with.

 Let's see the replace in action. We'll replace the letter "e" in spam with "Drew" """)

print(spam.replace("e", "Drew"))
