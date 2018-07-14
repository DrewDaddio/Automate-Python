# Walking a Directory Tree
# Walking is being able to go through all of the files & folders in a directory

print("""Example:
import os

for folderName, subfolders, filenames in os.walk('c:\\delicious'):
    # folderName will return the folder name of the directory specified. In this case it's c:\\delicious
    print('The folder is ' + folderName)
    # The subfolders will list all of the subfolders in the specified directory
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    # The filenames are all of the filenames in the specified directory
    print('The filenames in ' + folderName +  ' are: ' + str(filenames)
    # As this is a for loop the blank line print will make it easy to group the listings.
    print()""")

for folderName, subfolders, filenames in os.walk('c:\\delicious'):
    # folderName will return the folder name of the directory specified. In this case it's c:\\delicious
    print('The folder is ' + folderName)
    # The subfolders will list all of the subfolders in the specified directory
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    # The filenames are all of the filenames in the specified directory
    print('The filenames in ' + folderName +  ' are: ' + str(filenames)
    # As this is a for loop the blank line print will make it easy to group the listings.
    print()

    for subfolder in subfolders:
          if 'fish' in subfolder:
              os.rmdir(subfolder)

    for file in filenames:
          if file.endswith('.py':
                           shutil.copy(os.join(folderName, file). os.join(folderName, file + '.backup')
