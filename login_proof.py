from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from pprint import pprint
from time import sleep
from selenium.webdriver.support.relative_locator import with_tag_name
from selenium.webdriver.common.action_chains import ActionChains
import pytest

driver = Chrome ()
driver.get("https://parabank.parasoft.com/parabank/index.htm")

username= driver.find_element(By.XPATH,'//input[@name="username"]')
username.send_keys("john")

pwd= driver.find_element(By.XPATH,'//input[@name="password"]')
pwd.send_keys("demo")
    
login= driver.find_element(By.XPATH,'//input[@value="Log In"]')
login.click()

proof = driver.find_element(By.XPATH,'//p[contains(.,"John Smith")]')
# assert proof != None 
print(':'+proof.text+':')
# assert proof.text == "JohnZ SmithZ"

driver.quit()
    # ///p/b[text() = "Welcome"]
    # //p[contains(.,"John Smith")]

