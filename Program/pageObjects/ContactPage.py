from time import sleep

from pynput import keyboard
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller


class ContactPage:
    keyboard = Controller()
    button_contact_logo_xpath = "/html/body/header/nav/a[2]"
    button_create_xpath = "/html/body/div[3]/div/div[1]/div[2]/div[1]/div/div/button"

    radio_individual_xpath = '//*[@id="o_field_input_819"]/div[1]/label'
    radio_company_xpath = '//*[@id="o_field_input_819"]/div[2]/label'

    textbox_company_name_id = "o_field_input_915"
    textbox_street_id = "o_field_input_901"
    textbox_city_id = "o_field_input_903"
    dropDown_country_id = "o_field_input_906"
    textbox_phone_id = "o_field_input_853"
    textbox_email_id = "o_field_input_855"
    textbox_weblink_id = "o_field_input_856"
    textbox_tag_id = "o_field_input_859"

    nav_sales_and_purchase_xpath = "/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[6]/div[1]/ul/li[2]/a"
    dropDown_salePerson_id = "o_field_input_862"
    dropDown_salePerson_selector = 'aria/Sreyne CHOM[role="list"]'

    nav_InternalNote_xpath = "/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[6]/div[1]/ul/li[5]/a"
    textbox_note_id = "o_field_input_907"

    button_save_xpath = "/html/body/div[3]/div/div[1]/div[2]/div[1]/div/div/div[2]/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickContact(self):
        self.driver.find_element(By.XPATH, self.button_contact_logo_xpath).click()

    def clickCreate(self):
        self.driver.find_element(By.XPATH, self.button_create_xpath).click()

    def clickCompany(self):
        self.driver.find_element(By.XPATH, self.radio_company_xpath).click()

    def enterCompanyName(self, company_name):
        self.driver.find_element(By.ID, self.textbox_company_name_id).send_keys(company_name)

    def enterStreet(self, street):
        self.driver.find_element(By.ID, self.textbox_street_id).send_keys(street)

    def enterCity(self, city):
        self.driver.find_element(By.ID, self.textbox_city_id).send_keys(city)

    def enterCountry(self, country):
        self.driver.find_element(By.ID, self.dropDown_country_id).send_keys(country)
        sleep(1)
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)


    def enterPhone(self, phone):
        self.driver.find_element(By.ID, self.textbox_phone_id).send_keys(phone)

    def enterEmail(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def enterWebLink(self, link):
        self.driver.find_element(By.ID, self.textbox_weblink_id).send_keys(link)

    def enterTag(self, tag):
        self.driver.find_element(By.ID, self.textbox_tag_id).send_keys(tag)
        sleep(1)
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)


    def click_Sale_and_purchase(self):
        self.driver.find_element(By.XPATH, self.nav_sales_and_purchase_xpath).click()

    def enterSalePerson(self, person):
        self.driver.find_element(By.ID, self.dropDown_salePerson_id).send_keys(person)
        sleep(1)
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

    def click_Internal_note(self):
        self.driver.find_element(By.XPATH, self.nav_InternalNote_xpath).click()

    def enterNote(self, remark):
        self.driver.find_element(By.ID, self.textbox_note_id).send_keys(remark)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()

    def refreshPage(self):
        self.driver.refresh()
        sleep(2)


