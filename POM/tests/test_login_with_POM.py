import sys
sys.path.append("d:/Projects/QA_Tester/POM")

from selenium import webdriver
from pages.loginpage import loginPage as LP
import unittest

class LoginPage(unittest.TestCase):

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