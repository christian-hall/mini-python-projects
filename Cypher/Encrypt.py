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


def getKey(key):
    print("getting key for decryption")
    
def createKey():
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
    
    key = []
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
        key.append(printline)
        line_idx = line_idx + 1
    # add line 95, with the phrase v3h-S6XH2v&}W5b<w1n~ embedded. int 0 - 80
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
    key.append(printline)
    return key
    # concat a document of 95 lines, the last line being informaiton and the first 94 being gibberish with the key
    
key = createKey()
for k in key:
    print(k)
print()
print("Goodbye")