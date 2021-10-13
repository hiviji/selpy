from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from pprint import pprint
from time import sleep
from selenium.webdriver.support.relative_locator import with_tag_name
from selenium.webdriver.common.action_chains import ActionChains

try:

    driver = Chrome ()

    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    username= driver.find_element(By.XPATH,'//input[@name="username"]')
    username.send_keys("john")

    pwd= driver.find_element(By.XPATH,'//input[@name="password"]')
    pwd.send_keys("demo")

    login= driver.find_element(By.XPATH,'//input[@value="Log In"]')
    login.click()

    sleep(5)

    # total = driver.find_element(By.XPATH,'//table[@id="accountTable"]/tbody/tr/td/b[text()="Total"]/../../td[2]/b')
    # print(total.text)

    # total = driver.find_element(By.XPATH,'//table[@id="accountTable"]/tbody/tr/td/b[text()="Total"]/../following-sibling::td/b')
    # print(total.text)

    label = driver.find_element(By.XPATH,'//table[@id="accountTable"]/tbody/tr/td/b[text()="Total"]')
    print(label.tag_name)

    #relative locator - Selenium 4 - to the right of label
    value = driver.find_elements(with_tag_name("b").to_right_of(label))
    print(value[0].text)

    #verify 
    # driver.move_to_element(value)
    actions = ActionChains(driver)
    actions.move_to_element(value[0])
    actions.perform()
    assert((value[0].text) == "$1693.67")
    print("Test Passed")

except:
    
    print(" SORRY, THE TEST HAS FAILED")
    sleep(10)     
    driver.get_screenshot_as_file("cap1.png")
    print("screenshot captured")

finally:

    driver.quit()