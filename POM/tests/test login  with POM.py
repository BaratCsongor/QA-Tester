import sys
sys.path.append("d:\Projects\QA Tester\POM")

from selenium import webdriver
from pages.loginpage import loginPage as LP
from unittest import TestCase as TC
import unittest

class LoginPage(TC):

    def setUp(self):

        self.driver = webdriver.Chrome()
        
    def test_login_positive(self):
        
        loginPage = LP(self.driver)


        loginPage.goToLogin()
        loginPage.setUsername("student")
        loginPage.setPassword("Password123")
        loginPage.clickSubmit()
        loginPage.verifyTitle()

    def tearDown(self):
        self.driver.quit()


if __name__ =="__main__":
    unittest.main()