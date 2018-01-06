from lxml import html
import requests
from utilities import list_to_string

class Character:
    # This class handles the character informantion from the website
    def __init__(self, root):
        # XPath returns as array for all info. Method printInfo will deal with
        # the display of information and how it should look like to the user
        # The Xpath searches for the info necessary in the table on the tibia.com website

        table_address = '//*[@id=\"characters\"]/div[5]/div/div/table[1]/tr[td//text()'

        self.name = root.xpath(table_address + '[contains(., \'Name:\')]]/td[2]/text()')
        self.former_names = root.xpath(table_address + '[contains(., \'Former Names:\')]]/td[2]/text()')
        self.sex = root.xpath(table_address + '[contains(., \'Sex:\')]]/td[2]/text()')
        self.vocation = root.xpath(table_address + '[contains(., \'Vocation:\')]]/td[2]/text()')
        self.level = root.xpath(table_address + '[contains(., \'Level:\')]]/td[2]/text()')
        self.achievement_points = root.xpath(table_address + '[contains(., \'Achievement Points:\')]]/td[2]/text()')
        self.world = root.xpath(table_address + '[contains(., \'World:\')]]/td[2]/text()')
        self.former_world = root.xpath(table_address + '[contains(., \'Former World:\')]]/td[2]/text()')
        self.residence = root.xpath(table_address + '[contains(., \'Residence:\')]]/td[2]/text()')
        self.married_status = root.xpath(table_address + '[contains(., \'Married To:\')]]/td[2]/a/text()')
        self.house = root.xpath(table_address + '[contains(., \'House:\')]]/td[2]/a/text()')
        self.guild = root.xpath(table_address + '[contains(., \'Guild\')]]/td[2]/a/text()')
        self.last_login = root.xpath(table_address + '[contains(., \'Last Login:\')]]/td[2]/text()')
        self.account_status = root.xpath(table_address + '[contains(., \'Account\')]]/td[2]/text()')


    def print_info(self):
        # prints with if statements are optional for characters, else mandatory

        print ("Name: " + list_to_string(self, self.name))
        if self.former_names:
            print ("Former Names: " + list_to_string(self, self.former_names))
        print("Sex: " + list_to_string(self, self.sex))
        print("Vocation: " + list_to_string(self, self.vocation))
        print("Level: " + list_to_string(self, self.level))
        print("Achievement Points: " + list_to_string(self, self.achievement_points))
        print("World: " + list_to_string(self, self.world))
        if self.former_world:
            print("Former World: " + list_to_string(self, self.former_world))
        if self.residence:
            print("Residence: " + list_to_string(self, self.residence))
        if self.married_status:
            print("Married To: " + list_to_string(self, self.married_status))
        if self.house:
            print("House: " + list_to_string(self, self.house))
        if self.guild:
            print("Guild Membership: " + list_to_string(self, self.guild))
        print("Last Login: " + list_to_string(self, self.last_login))
        print("Account Status: " + list_to_string(self, self.account_status))

