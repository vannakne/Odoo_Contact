from time import sleep
from selenium.webdriver.common.by import By

class LoginPage:
    textBox_email_id = "login"
    textBox_password_id = "password"
    button_login_xpath = '//*[@id="wrapwrap"]/main/div/form/div[3]/button'

    def __init__(self, driver):
        self.driver = driver

    def enterEmail(self, email):
        self.driver.find_element(By.ID, self.textBox_email_id).send_keys(email)

    def enterPassword(self, passwd):
        self.driver.find_element(By.ID, self.textBox_password_id).send_keys(passwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

