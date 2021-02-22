import os
import random

def getRandomCharacters():
    # main cypher options
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
              '[', '{', ']', '}', '\\', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?']
    random_characters = []
    while len(characters) > 0:
        random_selection = random.choice(characters)
        random_characters.append(random_selection)
        characters.remove(random_selection)
    return random_characters

def getKey():
    print("getting base characters...")
    character_base = getRandomCharacters()
    print("getting code characters...")
    character_code = getRandomCharacters()
    print("creating key...")
    key = []
    while len(character_base) > 0 and len( character_code) > 0:
        random_base = random.choice(character_base)
        random_code = random.choice(character_code)
        key.append([random_base, random_code])
        character_code.remove(random_code)
        character_base.remove(random_base)
    return key

key = getKey()