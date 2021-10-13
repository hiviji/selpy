from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from pprint import pprint
driver = Chrome ()

driver.get("https://formy-project.herokuapp.com/checkbox")
cwp = driver.find_element(By.ID,'checkbox-1')
print(cwp.tag_name)
# print(dir(cwp))
print(cwp.is_selected())
cwp.click()
print(cwp.is_selected())

cwp = driver.find_element(By.TAG_NAME,'h1')
print(cwp.text)

driver.quit()