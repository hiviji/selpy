from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from pprint import pprint
driver = Chrome ()

driver.get("https://formy-project.herokuapp.com/radiobutton")
rb1 = driver.find_element(By.ID,'radio-button-1')
rb2 = driver.find_element(By.XPATH,'//input[@value="option2"]')


# print(rb1.is_selected() +  rb2.is_selected())
print(str(rb1.is_selected()) + " " + str(rb2.is_selected()))

rb2.click()
print(str(rb1.is_selected()) + " " + str(rb2.is_selected()))

driver.quit()