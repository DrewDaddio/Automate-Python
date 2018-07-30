# Screenshots & image recognition

import pyautogui

print("To take a screenshot use, pyautogui.screenshot(<location>)")
pyautogui.screenshot(r'c:\\users\\drew\\MyPythonScripts\\screenshot_example.png')
print(r'Now check: c:\users\drew\MyPythonScripts\screenshot_example.png')
print('I\'ve previously saved a screenshot of the calculator 7 key. We will use python to go to the location of the 7 key on screen.')
print('Easiest way to do this is to make sure the python shell is open and doesn\'t take up the full screen')
print('open the calculator and put it where the python shell screen isn\'t')
print('Let\'s print the location of the 7key')
pyautogui.locateOnScreen('c:\\users\\drew\\MyPythonScripts\\7key\\calc7Key.png')
print(pyautogui.locateOnScreen('c:\\users\\drew\\MyPythonScripts\\7key\\calc7Key.png'))
print("If none shows up then there is an issue")

print("To see the sushigoroundbot, then search for it on Github")
