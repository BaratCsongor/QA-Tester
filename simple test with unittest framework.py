from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from assertpy import soft_assertions, assert_that
import unittest

class test_searchbox(unittest.TestCase):

    def setUp(self):

        self.driver=webdriver.Chrome()
        self.driver.get("https://www.emag.ro/")

    def test_searchbox(self):

        searchBox = self.driver.find_element(By.ID,"searchboxTrigger" )
        searchBox.clear()
        searchBox.send_keys("mouse")
        searchBox.send_keys(Keys.ENTER)

        firstResult = self.driver.find_element(By.CLASS_NAME,"card-v2-thumb")
        firstResult.click()

        with soft_assertions():
            assert_that(self.driver.title).contains("Mouse")

    def tearDown(self):

        self.driver.quit()

if __name__=="__main__":
    unittest.main()