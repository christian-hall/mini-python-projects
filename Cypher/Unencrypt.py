import os

def unencrypt(input_file, keypath):
    success = False
    input_lines, key_lines = [], []
    if os.path.isfile(input_file) and os.path.isfile(keypath):
        # get key
        with open(keypath) as file:
            for line in file:
                key_lines.append(line)
        # get input file
        with open(input_file) as file:
            for line in file:
                input_lines.append(line)
        success = True
    # get key from keypath
    # unencrypt key to get unencryption
    # delete key automatically
    # unencrypt message and return
    
    return success
    
print("CYPH3R - A TEXT FILE ENCRYPTION APP - Unencryption")
print("==================================================")
print()
directory = "/Users/christian/Documents/cyph3r/"

input_file = directory + input("What is the name of the cyr file you are unencrypting: ") + ".cyr"
keypath = directory + "k3y_"+ input("What is k3y number (3 digits): ") + ".cyr"
print(input_file)
print(keypath)
if ".cyr.cyr" in input_file:
    input_file = input_file[:len(input_file) - 4]
success = unencrypt(input_file, keypath)
if success == True:
    print("Encryption successful")
else:
    print("Encryption Failed")
print()
print("Goodbye")