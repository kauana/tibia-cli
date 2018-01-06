import requests
from lxml import html

# parseCharacters returns the url already with the character's name on it
def parseCharacter(charName):
    index = 0
    while index < len(charName):
        if charName[index] == " ":
             charName = charName.replace(charName[index], "+")
        index = index + 1
    charURL = "https://secure.tibia.com/community/?subtopic=characters&name=" + charName
    return charURL

# getWebsiteInfo returns the html tree of the website given as the argument
def getWebsiteInfo(link):
    page = requests.get(link)
    tree = html.fromstring(page.content)
    return tree

def list_to_string(self, info_list):
    string = (', '.join(info_list))
    return string
