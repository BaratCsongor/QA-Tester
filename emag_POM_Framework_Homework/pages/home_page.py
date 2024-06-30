from assertpy import assert_that, soft_assertions
from locators.locators import HomeLocators as HL
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def goToHome(self):
        self.driver.get("https://emag.ro")
        self.driver.maximize_window()

    def verifyLogo(self):
        homepageLogo = self.driver.find_elements(*HL.homepageLogo)
        with soft_assertions():
            assert_that(homepageLogo).is_true()
        print("1")

    def verifyTitle(self):
        with soft_assertions():
            assert_that(self.driver.title).contains("eMAG.ro")
        print("\n2")
       
    def verifySearchbox(self):
        searchbox = self.driver.find_element(*HL.searchbox)
        searchbox.clear()
        searchbox.send_keys("keyboard")
        searchbox.send_keys(Keys.ENTER)
        result=self.driver.find_element(*HL.result)
        result.click()

        with soft_assertions():
            assert_that(self.driver.title).contains("Tastatura")
        print("\n3")




