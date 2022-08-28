import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from info import ids, ps

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.facebook.com")
elem = driver.find_element(By.ID, "email")
elem.send_keys(ids)
elem = driver.find_element(By.ID, "pass")
elem.send_keys(ps)
elem = driver.find_element(By.NAME, "login")
elem.click()

time.sleep(1)
driver.get("https://www.facebook.com/nhi.phan.583")
time.sleep(2)
driver.execute_script("window.scrollBy(0,1000)")
elem = driver.find_element(By.XPATH, """//span[text()='Like']""")
time.sleep(1)
elem.click()
time.sleep(10)
driver.close()
