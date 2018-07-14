# Files & Folders
# Chapter 8 of the textbook

# Files concepts:
# File path and File Name

print("""For Python to do backslashes then we can do multiple options in order to write the backslash :
1. We can do a double backslash - C:\\home\\Desktop\\test.txt
2. We can do similar to a regular expression - (r'C:\\home\\Desktop\\test.txt')
""")

print("We can also use the OS Module")

import os
print("""import os
print(os.path.join('Folder', 'folder2', 'folder3', 'file.png'))""")

print(os.path.join('Folder', 'folder2', 'folder3', 'file.png'))

print("""
os.sep
os.getcwd()
os.chdir('C:\\')""")

print(os.sep)
print(os.getcwd())
print(os.chdir('C:\\'))

print(""""Relative Paths vs. Absolute Paths
Absolute Paths: The full written file path
Relative Paths: are paths that are concise and have just the last 2 (approximately) needed""")

print("""Example:
os.chdir('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.5')
os.path.abspath('spam.png')
""")

print(os.path.abspath('spam.png'))

print("""Example to check if a path is an absolute path:
os.path.isabs('..\\..\\spam.png')
os.path.isabs('c:\\folder\\folder')

Example to check if a path is a relative path:
os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder')

Example to pull out the directory until the last part of the file path:
os.path.dirname('c:\\folder\\folder2\\spam.png

example to pull out the last part of the file path:
os.path.basename('c:\\folder1\\folder\\spam.png')
os.path.basename('c:\\folder1\\folder')
""")

print(os.path.isabs('..\\..\\spam.png'))
print(os.path.isabs('c:\\folder\\folder'))

print(os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder'))
print(os.path.dirname('c:\\folder\\folder2\\spam.png'))
print(os.path.basename('c:\\folder1\\folder\\spam.png'))
print(os.path.basename('c:\\folder1\\folder'))

print("""To check if a filepath exists, is a file, is a directory, and the file size:
os.path.exists('c:\\folder1\\folder2\\spam.png')
os.path.exists('c:\\')
os.path.isfile('c:\\folder1\\folder2\\spam.png')
os.path.isdir('c:\\')
os.path.getsize('c:\\windows\\system32\\calc.exe)
""")

print(os.path.exists('c:\\folder1\\folder2\\spam.png'))
print(os.path.exists('c:\\'))
print(os.path.isfile('c:\\folder1\\folder2\\spam.png'))
print(os.path.isdir('c:\\'))
print(os.path.getsize('c:\\windows\\system32\\calc.exe'))

print("""To create new folders:
os.makdirs('c:\\delicous\walnut\\coffee')""")
