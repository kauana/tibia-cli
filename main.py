from utilities import *
from character import Character

def main():
    characterName = input('What is the name of the character you want to search? ')
    charURL = parseCharacter(characterName)
    html = getWebsiteInfo(charURL)

    character = Character(html)
    character.print_info()

main()

