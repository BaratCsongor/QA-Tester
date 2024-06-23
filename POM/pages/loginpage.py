from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import loginLocators as logL 
from assertpy import soft_assertions, assert_that

class loginPage:

    def __init__(self,driver):

        self.driver = driver

    def goToLogin(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login")

    def setUsername(self, userValue):
         username = self.driver.find_element(*logL.username)
         username.clear()
         username.send_keys(userValue)

    def setPassword(self, passValue):
         username = self.driver.find_element(*logL.password)
         username.clear()
         username.send_keys(passValue)

    def clickSubmit(self):
        submit = self.driver.find_element(*logL.submit)
        submit.click()

    def verifyTitle(self):
         
         wait = WebDriverWait(self.driver,10)
         title =self.driver.find_element(*logL.title)

         with soft_assertions():
            assert_that(title).is_true()