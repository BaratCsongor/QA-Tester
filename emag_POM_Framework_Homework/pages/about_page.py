from assertpy import assert_that, soft_assertions
from locators.locators import AboutLocators 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class AboutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def goToAbout(self):
        self.driver.get("https://about.emag.ro/")  
        self.driver.maximize_window()
        
    def verifyTitle(self):
        with soft_assertions():
            assert_that(self.driver.title).contains("Bine ai venit la eMAG")


    def verifyNavigation(self):
        navList= self.driver.find_element(*AboutLocators.navList).find_elements(*AboutLocators.listItem)
   

        navItems = []
        
        for i in navList:
            navItems.append(i.text)

        with soft_assertions():
            assert_that(navItems).contains("Grupul eMAG", "eMAG Teams", "Sustenabilitate", "Media")  
