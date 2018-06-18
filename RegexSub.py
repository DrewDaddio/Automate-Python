# Regular Expression sub()

#RE compile(): create regular expression objects
#RE search(): search for objects
#RE findall(): findall matches

#RE sub(): substitute text; find and replace

import re

namesRegex = re.compile(r'Agent \w+')
#\w+ = word characters
example = 'Agent Alice gave the secret documents to Agent Bob.'
print(example)
print(namesRegex.findall(example))
print("Now let's redact the agents names")
print(namesRegex.sub('REDACTED', example))
print("Now let's change the agents  names to be identifiable but not personally identifiable")

redactRegex = re.compile(r'Agent (\w)\w*')
print("redactRegex = re.compile(r'Agent (\w)\w*')")
print(redactRegex.findall(example))
print("redactRegex.sub(r'Agent \1****', example)")
print(redactRegex.sub(r'Agent \1****', example))

print("redactRegex.sub(r'Agent \1', example)")
print(redactRegex.sub(r'Agent \1', example))

print("Now verbose mode, to show the phone number")

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print("Example: phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') \nNow we'll look at it in verbose mode")

re.compile(r'''
(\d\d\d-)|    # area code (without parens, with dash)
(\(\d\d\d\) ) # -or- area code with parens and no dash 
\d\d\d   # first 3 digits
\d\d\d\d # last 4 digits
\sx\d[2,4] # extension, like x1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE )

print("The | Pipe bitwise operator allows the use of multiple regular expressions")
      
print("""re.compile(r'''
(\d\d\d-)|    # area code (without parens, with dash)
(\(\d\d\d\) ) # -or- area code with parens and no dash 
\d\d\d   # first 3 digits
\d\d\d\d # last 4 digits
\sx\d[2,4] # extension, like x1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE )""")
