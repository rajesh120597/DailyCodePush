from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
UN = driver.find_element(By.ID, "user-name")
UN.send_keys("standard_user")
PW = driver.find_element(By.ID, "password")
PW.send_keys("secret_sauce")
LB = driver.find_element(By.ID, "login-button")
LB.click()
assert driver.title == "Swag Labs"
driver.find_element(By.ID, "react-burger-menu-btn").click()
driver.find_element(By.ID, "logout_sidebar_link").click()








