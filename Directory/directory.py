# This project is just a simple tool to navigate through the computer
# files. It will dynamically list optional files next to numbers, then
# display them alphabetically. At the end is the "back" option. This
# program will read if the system is a MacOS or Windows computer for
# help.

from sys import platform
import os

if platform == "darwin" or platform == 'linux' or platform == 'linux2':
    directory = '/'
elif platform == 'win32':
    directory = 'c:/'
else:
    print('OS not recognized')

if os.path.isdir(base_directory):
    print('Successfully Initialized')
else:
    print('Initialization Failed')


# _______________________"/"_______________________
# | 1. Applications                               |
# | 2. Library                                    | 
# | 3. System                                     |
# | 4. Users                                      |
# | 5. Volumes                                    |
# | B  Back                                       |
# | E  Exit                                       |
# -------------------------------------------------

# Get a list of directories and compound them in an array

# Build and parse the directory string based on choices
# directory = getnewdirectory(directory, choice)