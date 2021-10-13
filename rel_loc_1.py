from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from pprint import pprint
from selenium.webdriver.support.relative_locator import with_tag_name

driver = Chrome ()

driver.get("https://demoqa.com/sortable")

rl1=driver.find_element(By.XPATH,'//div[@class="vertical-list-container mt-4"]/div[3]')

print(rl1.text)

#relative locator above
rla= driver.find_elements(with_tag_name("div").above(rl1))

print(rla[1].tag_name)

print(rla[1].text)

driver.quit()