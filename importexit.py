import sys
#import command will import the module 'sys'
print('Hello')
sys.exit()
#.exit() will cause the module to exit
print('Goodbye')

#doing any "module".command() will cause the imported module to run the command that is located within the module
# to install 3rd party modules: do it through the "pip" module
# http://automatetheboringstuff.com/appendixa/

import pyperclip
#pyperclip has a copy and paste function for pasting from the clipboard
pyperclip.copy('Hello world!')
#.copy: Copies the text to the clipboard. In this case it will copy "Hello world!" to the clipboard
pyperclip.paste()
#.paste: pastes what's in the clipboard
