import path_config
from selenium import webdriver
import unittest
from pages.home_page import HomePage as HP

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_logo(self):
        homepage = HP(self.driver)
        homepage.goToHome()
        homepage.verifyLogo()
      

    def test_title(self):
        homepage = HP(self.driver)
        homepage.goToHome()
        homepage.verifyTitle()
       

    def test_searchbox(self):
        homepage = HP(self.driver)
        homepage.goToHome()
        homepage.verifySearchbox()
      

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()    
