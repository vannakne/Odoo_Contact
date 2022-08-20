import configparser

config = configparser.RawConfigParser()
config.read("../Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getAppUrl():
        return "https://edu-mkit.odoo.com/web/login#id=&action=462&model=res.partner&view_type=form&cids=1&menu_id=310"

    @staticmethod
    def getEmail():
        with open("../../Email_Password.txt", 'r') as file:
            email = file.readline()
            password = file.readline()
        return email, password

    @staticmethod
    def getPassword():
        with open("../../Email_Password.txt", 'r') as file:
            password = file.readline()
        return password

print(ReadConfig.getEmail())
print(ReadConfig.getPassword())