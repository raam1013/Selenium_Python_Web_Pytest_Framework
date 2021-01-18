from selenium import  webdriver
from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import logging
class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//input[@class='button-1 login-button'][@type='submit']"
    link_logout_link_text = "Logout"


    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        time.sleep(4)
        user = self.driver.find_element_by_id(self.textbox_username_id)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", user,
                                   "background: yellow; border: 2px solid red;")
        user.send_keys(username)

        time.sleep(5)

    def setPasswordName(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        time.sleep(5)
        pasword = self.driver.find_element_by_id(self.textbox_password_id)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", pasword,
                                   "background: yellow; border: 2px solid red;")
        pasword.send_keys(password)

        time.sleep(5)


    def clickLogin(self):
        login = self.driver.find_element_by_xpath(self.button_login_xpath)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", login,
                                   "background: yellow; border: 2px solid red;")
        login.click()
        time.sleep(5)


    def clickLogout(self):
        logout = self.driver.find_element_by_link_text(self.link_logout_link_text)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", logout,
                                   "background: yellow; border: 2px solid red;")
        logout.click()
        time.sleep(5)

