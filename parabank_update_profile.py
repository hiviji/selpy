from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from pprint import pprint
from time import sleep
from selenium.webdriver.support.relative_locator import with_tag_name

driver = Chrome ()

driver.get("https://parabank.parasoft.com/parabank/index.htm")

username= driver.find_element(By.XPATH,'//input[@name="username"]')
username.send_keys("john")

pwd= driver.find_element(By.XPATH,'//input[@name="password"]')
pwd.send_keys("demo")

login= driver.find_element(By.XPATH,'//input[@value="Log In"]')
login.click()

#by Xpath
# update = driver.find_element(By.XPATH,'//p[@class="smallText"]/../ul/li/a[text()="Update Contact Info"]')

#link text 
# update = driver.find_element(By.LINK_TEXT,"Update Contact Info")

#partial link text 
update = driver.find_element(By.PARTIAL_LINK_TEXT,"Update")

update.click()

# state = driver.find_element(By.XPATH,'//table[@class="form2"]/tbody/tr/td/b[text()="State:"]')
state = driver.find_element(By.XPATH,'//b[text()="State:"]')
print(state.text)

state_input = driver.find_element(By.XPATH,'//input[@name="customer.address.state"]')
print(state_input.text)
state_input.send_keys("NJ")
sleep(10)
print(state_input.text)


# DO NOT USE - ITS BULLSHIT 
# state_value = driver.find_elements(with_tag_name("input").to_right_of(state))
# print(len(state_value))
# print(state_value[0].text)

driver.quit()