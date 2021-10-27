#from selenium import webdriver
#from selenium.webdriver import Chrome
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.relative_locator import with_tag_name
#from selenium.webdriver.common.action_chains import ActionChains
#import pytest

from pprint import pprint
from time import sleep
from src.testproject.sdk.drivers import webdriver

driver = webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/index.htm")


def test_login():
    print("***Starting Tests***")

    username= driver.find_element(By.XPATH,'//input[@name="username"]')
    username.send_keys("john")

    pwd= driver.find_element(By.XPATH,'//input[@name="password"]')
    pwd.send_keys("demo")
     
    login= driver.find_element(By.XPATH,'//input[@value="Log In"]')
    login.click()

    proof = driver.find_element(By.XPATH,'//p[contains(text(),"John Smith")]')
    assert proof is not None 
    # print(':'+proof.text+':')
    # assert proof.text == "JohnZ SmithZ"
    # driver.quit()
    sleep(10)

    # ///p/b[text() = "Welcome"]
    # //p[contains(.,"John Smith")]
    

def test_total():
   
    label = driver.find_element(By.XPATH,'//table[@id="accountTable"]/tbody/tr/td/b[text()="Total"]')
    # print(label.tag_name)

    #relative locator - Selenium 4 - to the right of label
    value = driver.find_elements(with_tag_name("b").to_right_of(label))
    # print(value[0].text)

    #verify 
    # driver.move_to_element(value)
    actions = ActionChains(driver)
    actions.move_to_element(value[0])
    actions.perform()
    assert((value[0].text) == "$1192.67")
    driver.quit()

def test_three():
    assert 10 == 10

def test_four():
    assert 10

def test_five():
    raise AssertionError("Test Five failed as expected")
    # assert True
