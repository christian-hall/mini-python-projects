# This project is just a simple tool to navigate through the computer
# files. It will dynamically list optional files next to numbers, then
# display them alphabetically. At the end is the "back" option. This
# program will read if the system is a MacOS or Windows computer for
# help.

from sys import platform
import os

def generate_menu(directory, files):
    MAX_WIDTH, title = 60, ' ' + directory + ' '
    while len(title) <= 60:
        if len(title) % 2 == 0:
            title = "-" + title
        else:
            title = title + "-"
    print(title)
    idx = 0
    for file in files:
        print(str(idx) + ' : ' + file)
        idx = idx + 1
    print ('b : GO BACK\ne : EXIT APP\n------------------------------------------------------------')

def get_choices(directory):
    files = os.listdir(directory)
    for file in files:
        if '.' in file:
            files.remove(file)
    generate_menu(directory, files)
    choice = input('Selection: ')
    if choice.isnumeric():
        print("number recognized")
    else:
        
    if choice == 'b':
        print('GO BACK')
        # split the string at the second-to-last slash 
        # if directory == '/' or 'c:/' this will be ignored
    elif choice == 'e' or choice == 'E':
        directory = 'e'
    elif type(choice) == 'int':
        print('Numeber selected')
        # get the directory based on the idx of the files
        # check if file is directory, if it is, then list items there, if not, then delete file from array
    return directory

if platform == "darwin" or platform == 'linux' or platform == 'linux2':
    directory = '/'
elif platform == 'win32':
    directory = 'c:/'
else:
    print('OS not recognized')
if os.path.isdir(directory):
    while directory != 'e':
        print('Successfully Initialized')
        directory = get_choices(directory)
else:
    print('Initialization Failed')




# _______________________"/"_______________________
# | 1 : Applications                               |
# | 2 : Library                                    | 
# | 3 : System                                     |
# | 4 : Users                                      |
# | 5 : Volumes                                    |
# | B : Back                                       |
# | E : Exit                                       |
# -------------------------------------------------

# Get a list of directories and compound them in an array

# Build and parse the directory string based on choices
# directory = getnewdirectory(directory, choice)

