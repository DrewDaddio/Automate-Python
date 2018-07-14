# Reading and Writing Plain Text Files

print("""Steps to reading and writing text files in Python:
Open
1. open() function: open's the file

helloFile = open('<file name.txt>')
helloFile.read()
helloFile.close()

Read
2. readlines() method: returns all of the lines as strings inside of a list.

helloFile = open('<file name.txt>')
helloFile.readlines()
helloFile.close()

Write mode
1. helloFile = open('<file name.txt>', 'w') # the w will turn the function into write mode. Write mode will overwrite items in the text file.
helloFile.read()
helloFile.close()

Append mode
1. helloFile = open('<file name.txt>', 'a') # the w will turn the function into append mode. Append mode will add on to the file.
helloFile.read()
helloFile.close()

For both the write & append mode then it will automatically create the file.
helloFile.write(<text input>)
helloFile.close()

Relative filepath: If you don't put a directory in write mode then it will use the current working directory

Shelve Module
Used to save variables (list, dictionaries, complex data files) into the python program to binary shelf files using  the shelve module.
Then in the future you can call back to shelved data in order to use the it. They are stored as .bak, .dat, .dir file types. The files are binary files so they cannot be read in notepad.

import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['zophie, 'Pooka', 'Simon', 'Fat-tail', 'Cleo]
shelfFile.close()

Keys Method
shelfFile = shelve.open('mydata')
shelfFile.keys
.ist(shelfFile.keys())
list(shelfFile.values())

""")
