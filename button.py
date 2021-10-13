from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint
from time import sleep

driver = Chrome ()

driver.get("https://formy-project.herokuapp.com/buttons")

# button1 = driver.find_element(By.CLASS_NAME,'btn-info')
# button1 = driver.find_element(By.CSS_SELECTOR,'.btn.btn-lg.btn-info')
# button1 = driver.find_element(By.XPATH,'//button[@class="btn btn-lg btn-info"]')
button1 = driver.find_element(By.CSS_SELECTOR,'button[class="btn btn-lg btn-info"]')
print(button1.is_selected())
# button1.click()
# driver.execute_script("arguments[0].click();",button1)
sleep(60)
button1.send_keys(Keys.ENTER)

print(dir(button1))

print(button1.is_selected())
sleep(60)

driver.quit()