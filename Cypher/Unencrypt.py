import os

def unencrypt(filepath, keypath):
    success = False
    # get key from keypath
    # unencrypt key to get unencryption
    # delete key automatically
    # unencrypt message and return
    
    return success
    
print("CYPH3R - A TEXT FILE ENCRYPTION APP - Unencryption")
print("==================================================")
print()
directory = "/Users/christian/Documents/cyph3r/"

filepath = directory + input("What is the name of the cyr file you are encrypting: ") + ".cyr"
keypath = directory + input("What is k3y number (k3y_???.cyr): ") + ".cyr"
if ".cyr.cyr" in input_file:
    input_file = input_file[:len(input_file) - 4]
success = unencrypt(filepath, keypath)
if success == True:
    print("Encryption successful")
else:
    print("Encryption Failed")
print()
print("Goodbye")