# Deleting Files

print("""Delete Files
3 ways:

OS Module

import os
os.unlink('bacon.txt') # This is passed through a relative path

os.getcwd() # Get the current working directory for the relative path

os.rmdir('c:\\delicious') # rmdir is Remove Directory; The directory has to be completely empty before the directory is directory

Shell Utility Module
import shutil
shutil.rmtree('c:\\delicious') # This will delete the directory and all files within it.

All of these will be deleted and skip going to the recycle bin

How to do a Dry Run Example

import os

for filename in os.list():
    if filename.endswith('.rxt'):
        #os.unlink(filename) # The deletion command is commented out in the dry run so we don't do damage while it's being tested but we know that it's there.
        print(filename) # this was created as an output for the test. It will print the files identified for deletion instead of deleting them

The Send2Trash Module
# Will need to install this module through pyp
#will send files / folder to the recylcing bin

send2trash.send2trash()
""")
