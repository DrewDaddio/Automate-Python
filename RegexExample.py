#! python3
# Regex Example: Phone and Email Scraper

#PDF: http://cdm266101.cdmhost.com/cdm/ref/collection/p266101coll7/id/25785
#Directory of Arkansas higher education personnel, 2015

print("First, we'll start by scraping the PDF \"Directory of Arkansas higher education personnel, 2015\"")

import re, pyperclip

# Create a regex for phone numbers

phoneRegex = re.compile(r'''
# Phone number examples: 415-555-0000, 555-0000, (415) 555-0000, 555-000 ext 12345, ext. #, x12345

(
((\d\d\d) | (\(\d\d\d\)))?               # area code (optional)
(\s|-)                                                      # First separator
\d\d\d                                                  # first 3 digits
-                                                              # Seperator
\d\d\d\d                                            # last 4 digits
(((ext(\.)?\s) |x)                                  # extension word-part (optional)
(\d{2,5}))?                                             # extention number-part (optional)
)
''', re.VERBOSE)

print("""phoneRegex = re.compile(r'''
# Phone number examples: 415-555-0000, 555-0000, (415) 555-0000, 555-000 ext 12345, ext. #, x12345

((\d\d\d) | (\(\d\d\d\)))?               # area code (optional)
(\s|-)                                                      # First separator
\d\d\d                                                  # first 3 digits
-                                                              # Seperator
\d\d\d\d                                            # last 4 digits
(((ext(\.)?\s) |x)                                  # extension word-part (optional)
(\d{2,5}))?                                             # extention number-part (optional)
''', re.VERBOSE)""")

# TODO: Create a regex for email addresses

emailRegex = re.compile(r'''
#some.+_thing@(\d{2,5}))?.com
[a-zA-Z0-9_.+]+                                     # name part
@                                                               # @ symbol
[a-zA-Z0-9_.+]+                                   # Domain name part


''', re.VERBOSE)

# TODO: Get the text off the clipboard

# TODO: Copy the extracted email/phone to the clipboard

text = pyperclip.paste()
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

testPhoneNumbers = []
for phoneNumber in extractedPhone:
    testPhoneNumbers.append(phoneNumber[0])
    

print(extractedPhone)
print(testPhoneNumbers)
# To put all numbers on separate lines
allPhoneNumbers = '\n'.join(testPhoneNumbers)
results = allPhoneNumbers + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
print(results)
print("Open Word or Notepad++ and try to paste. The emails and phone numbers should print out!")
