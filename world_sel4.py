from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.worldometers.info/world-population')

# header = driver.find_element_by_class_name('maincounter-number')
header = driver.find_element(By.CSS_SELECTOR,'.maincounter-number')

print(header.text)

# spans = header.find_elements_by_class_name('rts-nr-int')
spans = header.find_elements(By.CLASS_NAME,'rts-nr-int')

digits = [s.text for s in spans]
population = ','.join(digits)
print('POPULATION', population)

sleep(100)

driver.quit()
