from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from assertpy import soft_assertions, assert_that

class loginPage:

    def __init__(self,driver):

        self.driver = driver

    def goToLogin(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login")

    def setUsername(self):
         username = self.driver.find_element(By.ID,"username")
         username.clear()
         username.send_keys("student")

    def setPassword(self):
         username = self.driver.find_element(By.ID,"password")
         username.clear()
         username.send_keys("Password123")

    def clickSubmit(self):
        submit = self.driver.find_element(By.ID,"submit")
        submit.click()

    def verifyTitle(self):
         
         wait = WebDriverWait(self.driver,10)
         title = wait.until(EC.presence_of_element_located((By.TAG_NAME,"h1")))

         with soft_assertions():
            assert_that(title).is_true()