# Copying and moving files and folders.

print("""Copy Function
Shell Utilities Module has the ability to copy, move, rename & delete folders within your python progams.

python code:
import shutil
shutil.copy('c:\\spam.txt', 'c:\\delicious')

This will copy the file into the "delicious folder"

shutil.copy('c:\\spam.txt', 'c:\\delicious\\spamspamspam.txt')

this will copy the file and rename it from spam.txt to spamspamspam.txt

In order to copy an entire folder (all files & subfolders within.

shutil.copytree('c:\\delicious', 'c:\\delicious_backup')

This copies the delicous folder to the delicious backup folder.

shutil.move('c:\\spam.txt', 'c:\\delicious\\walnut')

Will move the file within the folder to  the delicous\walnut folder.

shutil.move('c:\\delicious\\walnut\\spam.txt, 'c:\\delicious\\walnut\\eggs.txt')

Will move and rename the spam file to eggs.

