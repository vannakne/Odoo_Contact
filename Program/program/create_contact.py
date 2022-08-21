from time import sleep

from Program.utilities import XLUtils
from Program.pageObjects.ContactPage import ContactPage
from Program.pageObjects.LoginPage import LoginPage


class Test_login:
    url = "https://edu-mkit.odoo.com/web#action=462&model=res.partner&view_type=kanban&cids=1&menu_id=310"
    with open('../../Email_Password.txt') as file:
        email_login = file.readline()
        password = file.readline()

    print(email_login)
    print(password)

    path = '../../excel/Contact.xlsx'
    sheetName = 'Sheet1'


    def test_login(self, setup):

        self.driver = setup
        self.lp = LoginPage(self.driver)
        print("Ulr: ", self.url)
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(1)

        self.lp.enterEmail(self.email_login)
        self.lp.enterPassword(self.password)
        self.lp.clickLogin()
        sleep(7)
        self.contact = ContactPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, self.sheetName)
        Done = False

        for r in range(2, self.rows+1):
            self.contact.clickCreate()
            sleep(3)

            if XLUtils.readData(self.path, self.sheetName, r, 1) != None:
                self.company_name = XLUtils.readData(self.path, self.sheetName, r, 1)
                if XLUtils.readData(self.path, self.sheetName, r+1, 1) == None:
                    Done = True
            else:
                self.company_name = ''

            if XLUtils.readData(self.path, self.sheetName, r, 2) != None:
                self.street = XLUtils.readData(self.path, self.sheetName, r, 2)
            else:
                self.street = ''

            if XLUtils.readData(self.path, self.sheetName, r, 3) != None:
                self.city = XLUtils.readData(self.path, self.sheetName, r, 3)
            else:
                self.city = ''

            if XLUtils.readData(self.path, self.sheetName, r, 4) != None:
                self.country = XLUtils.readData(self.path, self.sheetName, r, 4)
            else:
                self.country = ''

            if XLUtils.readData(self.path, self.sheetName, r, 5) != None:
                 self.phone = XLUtils.readData(self.path, self.sheetName, r, 5)
            else:
                self.phone = ''

            if XLUtils.readData(self.path, self.sheetName, r, 6) != None:
                self.email = XLUtils.readData(self.path, self.sheetName, r, 6)
            else:
                self.email = ''

            if XLUtils.readData(self.path, self.sheetName, r, 7) != None:
                self.weblink = XLUtils.readData(self.path, self.sheetName, r, 7)
            else:
                self.weblink = ''

            if XLUtils.readData(self.path, self.sheetName, r, 8) != None:
                self.tag = XLUtils.readData(self.path, self.sheetName, r, 8)
            else:
                self.tag = ''

            if XLUtils.readData(self.path, self.sheetName, r, 9) != None:
                self.salePerson = XLUtils.readData(self.path, self.sheetName, r, 9)
            else:
                self.salePerson = ''

            if XLUtils.readData(self.path, self.sheetName, r, 10) != None:
                self.note = XLUtils.readData(self.path, self.sheetName, r, 10)
            else:
                self.note = ''

            self.contact.enterCompanyName(self.company_name)
            self.contact.enterStreet(self.street)
            self.contact.enterCity(self.city)
            self.contact.enterCountry(self.country)
            self.contact.enterPhone(self.phone)
            self.contact.enterEmail(self.email)
            self.contact.enterWebLink(self.weblink)
            self.contact.enterTag(self.tag)

            self.contact.click_Sale_and_purchase()
            sleep(1)
            self.contact.enterSalePerson(self.salePerson)

            self.contact.click_Internal_note()
            sleep(1)
            self.contact.enterNote(self.note)

            self.contact.clickSave()
            sleep(2)

            self.contact.clickContact()
            sleep(2)
            if Done == True:
                self.contact.enterDone()
                break
            self.contact.refreshPage()
            sleep(2)




























