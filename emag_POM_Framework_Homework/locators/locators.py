from selenium.webdriver.common.by import By

class HomeLocators:
    homepageLogo =(By.XPATH,"//*[@id='masthead']/div/div/div[1]/a/img")
    searchbox =(By.ID,"searchboxTrigger")
    result = (By.CLASS_NAME,"card-v2")


class AboutLocators:
    navList = (By.XPATH,"//*[@id='site-header']/div[1]/div/div[2]/ul")
    listItem = (By.TAG_NAME,"li")