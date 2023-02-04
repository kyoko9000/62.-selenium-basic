import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from info import ids, ps

# Creating Instance
option = Options()

# Working with the 'add_argument' Method to modify Driver Default Notification
option.add_argument('--disable-notifications')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, chrome_options= option)

driver.get("https://www.facebook.com")
time.sleep(1)
elem = driver.find_element(By.ID, "email")
elem.send_keys(ids)
elem = driver.find_element(By.ID, "pass")
elem.send_keys(ps)
elem = driver.find_element(By.NAME, "login")
elem.click()

time.sleep(5)
driver.get("https://www.facebook.com/profile.php?id=100084521482536")
time.sleep(5)
driver.execute_script("window.scrollBy(0,2000)")
elem = driver.find_element(By.XPATH, """//span[text()='Like']""")
time.sleep(2)
ActionChains(driver).click_and_hold(elem).perform()
time.sleep(2)
ActionChains(driver).move_to_element_with_offset(elem, 0, -30).click().perform()
# elem.click()
time.sleep(5)
driver.close()
driver.quit()
