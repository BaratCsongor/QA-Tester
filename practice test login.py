from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from assertpy import soft_assertions, assert_that


driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login")


wait = WebDriverWait(driver, 10) 

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password") 
submit = driver.find_element(By.ID, "submit")

username.clear()
username.send_keys("student")
password.clear()
password.send_keys("Password123")
submit.click()


welcomeMessage = wait.until(EC.presence_of_element_located((By.TAG_NAME,"h1")))
print("Mesajul principal este:", welcomeMessage.text)
with soft_assertions():
    # Verifica daca Url-ul contine "practicetestautomation.com/logged-in-successfully/"
    assert_that(driver.current_url).contains("practicetestautomation.com/logged-in-successfully/")

    # Verifica daca mesajul de intampinare contine cuvantul "Succesfully"
    assert_that(welcomeMessage.text).contains("Successfully")
    
    # Verifica prezenta butonului Logout
    assert_that(driver.find_element(By.XPATH, "//*[@id='loop-container']/div/article/div[2]/div/div/div/a")).is_true()