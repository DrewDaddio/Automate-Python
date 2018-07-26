# Downloading Files: Requests Modules
#Request module is a 3rd party module
# Need to install visit pip

import requests
# The get function will download based off the URL string inputted
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#status_code attribute will show the status
#Status 200 = Download OK
print(res.status_code)
# raise_for_status() will show the status of the download
# you can send the status to a plain text file
print(raise_for_status)
print(res.text[:500])
#open will save the status
playFile = open('RandJ.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
