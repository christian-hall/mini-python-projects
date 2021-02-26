import os
import random

def getRandomCharacters():
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
              '[', '{', ']', '}', '\\', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', ' ']
    random_characters = []
    while len(characters) > 0:
        random_selection = random.choice(characters)
        random_characters.append(random_selection)
        characters.remove(random_selection)
    return random_characters
    
def encrypt(directory, input_file):
    success = False
    character_base = getRandomCharacters()
    character_code = getRandomCharacters()
    
    char_key = []
    
    while len(character_base) > 0 and len( character_code) > 0:
        random_base = random.choice(character_base)
        random_code = random.choice(character_code)
        char_key.append([random_base, random_code])
        character_code.remove(random_code)
        character_base.remove(random_base)
    
    base_idx, code_idx = 1,1
    
    while base_idx == code_idx:
        base_idx, code_idx = random.randint(0, 101), random.randint(0, 101)
    
    cypher_key = []
    line_idx = 0
    while (line_idx < 94):
        char_idx = 0
        printline = ""
        while char_idx < 100:
            if char_idx == base_idx:
                char_key_entry = char_key[line_idx]
                printline = printline + char_key_entry[0]
            elif char_idx == code_idx:
                char_key_entry = char_key[line_idx]
                printline = printline + char_key_entry[1]
            else:
                printline = printline + random.choice(getRandomCharacters())
            char_idx = char_idx + 1
        cypher_key.append(printline)
        line_idx = line_idx + 1

    key_idx, char_idx, printline = random.randint(-1, 80), 0, ""
    while char_idx < 81:
        if char_idx == key_idx:
            key_phrase = "v3h-S6XH2v&}W5b<w1n~"
            coded_key_phrase = ""
            for key_phrase_char in key_phrase:
                for char_key_entry in char_key:
                    if key_phrase_char == char_key_entry[0]:
                        coded_key_phrase = coded_key_phrase + char_key_entry[1]
            printline = printline + coded_key_phrase
        else:
            printline = printline + random.choice(getRandomCharacters())
        char_idx = char_idx + 1
    cypher_key.append(printline)
    
    if os.path.isdir(directory) and os.path.isfile(input_file):
        key_output_file = directory + "k3y_" + str(random.randint(99, 1000)) + ".cyr"
        file = open(key_output_file, "a")
        for key in cypher_key: 
            file.write(key + '\n')
        file.close()
        
        output_text = []
        with open(input_file) as file:
            for line in file:
                newline = ""
                for character in line:
                    for char_key_entry in char_key:
                        if character == char_key_entry[0]:
                            newline = newline + char_key_entry[1]
                output_text.append(newline)
        file.close
            
        # create an output file and add each line, line-by line
        output_file = input_file[:len(input_file) - 4] + ".cyr"
        file = open(output_file, "a")
        for line in output_text:
            file.write(line + '\n')
        file.close()
    
        success = True
            
    return success

print("CYPH3R - A TEXT FILE ENCRYPTION APP")
print("===================================")
print()

directory = "/Users/christian/Documents/cyph3r/"
input_file = directory + input("What is the name of the text file you are encrypting: ") + ".txt"
if ".txt.txt" in input_file:
    input_file = input_file[:len(input_file) - 4]
success = encrypt(directory, input_file)
if success == True:
    print("Encryption successful")
else:
    print("Encryption Failed")
print()
print("Goodbye")