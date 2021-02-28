import os

def unencrypt(input_file, keypath):
    success = False
    input_lines, key_lines = [], []
    if os.path.isfile(input_file) and os.path.isfile(keypath):
        # get key
        with open(keypath) as file:
            for line in file:
                key_lines.append(line)
        coded_line = key_lines[-1]
        del key_lines[-1]
        base_idx = 0
        while base_idx < len(key_lines):
            cypher_key = []
            code_idx = 0
            while code_idx < len(key_lines[1]):                
                if code_idx == base_idx:
                    pass
                else:
                    for key_line in key_lines:
                        base_key = key_line[base_idx]
                        code_key = key_line[code_idx]
                        cypher_key.append([base_key, code_key])
                        #attempt to decode coded_line
                    decoded_line = ""
                    for character in coded_line:
                        for cypher_line in cypher_key:
                            if character == cypher_line[1]:
                                decoded_line = decoded_line + str(cypher_line[0])
                    if "v3h-S6XH2v&}W5b<w1n~" in decoded_line:
                        success = True
                        break       
                code_idx = code_idx + 1
            base_idx = base_idx + 1
            if success == True:
                break
        # get input file
        with open(input_file) as file:
            for line in file:
                input_lines.append(line)
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
if ".cyr.cyr" in input_file:
    input_file = input_file[:len(input_file) - 4]
success = unencrypt(input_file, keypath)
if success == True:
    print("Encryption successful")
else:
    print("Encryption Failed")
print()
print("Goodbye")